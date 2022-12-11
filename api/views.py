from django.http import JsonResponse
from unidecode import unidecode
import translators.server as ts
import geopy.distance
from django.contrib.gis.geoip2 import GeoIP2
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from ipware import get_client_ip
from datetime import datetime, timedelta
from .models import Appointment, Branch, AppointmentSchedule
from .serializers import BranchSerializer


def add_minutes(time: datetime, minutes: int) -> datetime:
  return time + timedelta(minutes=minutes)

def get_interval(time: datetime) -> dict:
  return {
    'dateTimeStart': time, 
    'dateTimeEnd': add_minutes(time, 30)
  }

# VIEWS
def get_user_location(request):
  g = GeoIP2()
  client_ip, _ = get_client_ip(request)
  city = unidecode(ts.google(g.city(client_ip)['city'], to_language='ro'))
  latitude = g.city(client_ip)['latitude']
  longitude = g.city(client_ip)['longitude']
  return JsonResponse({'city': city, 'latitude': latitude, 'longitude': longitude })

def get_cities(request):
  cities = [item.city for item in  Branch.objects.all()]
  return JsonResponse({'cities': sorted(list(set(cities)))})

def get_close_branches(request):
  distance_radius = float(request.GET.get('radius'))
  user_coords = (float(request.GET.get('lat')), float(request.GET.get('long')))
  all_branches = Branch.objects.all()

  result = []
  for branch in all_branches:
    branch_coords = (branch.latitude, branch.longitude)
    if (geopy.distance.geodesic(user_coords, branch_coords)).km <= distance_radius:
      result.append(BranchSerializer(branch).data)

  return JsonResponse({'branches': result})


def get_available_intervals(request, unit_id):
  start_time = datetime.now().replace(minute=0, hour=0, second=0, microsecond=0) # luam din request
  branch = Branch.objects.get(pk=unit_id)
  branch_schedule = branch.appointment_schedule

  result = {"availableTimeList": []}
  for i in range(0, 14):
    current_day = start_time + timedelta(days=i)
    lunch_start = (start_time + timedelta(days=i)).replace(hour=branch_schedule.lunch_break_start_hour, minute=branch_schedule.lunch_break_start_min)
    lunch_end = (start_time + timedelta(days=i)).replace(hour=branch_schedule.lunch_break_end_hour, minute=branch_schedule.lunch_break_end_min)
    day_end = (start_time + timedelta(days=i)).replace(hour=branch_schedule.mon_fri_end_hour, minute=branch_schedule.mon_fri_end_min)
    today_timeslots = {'day': current_day.replace(hour=0, minute=0, second=0, microsecond=0), 'timeSlots': []}

    current_day = current_day.replace(hour=branch_schedule.mon_fri_start_hour, minute=branch_schedule.mon_fri_start_min, second=0, microsecond=0)
    if (current_day.strftime("%A").startswith('S')):
      current_day = current_day.replace(hour=branch_schedule.sat_sun_start_hour, minute=branch_schedule.sat_sun_start_min, second=0, microsecond=0)
      day_end = day_end.replace(hour=branch_schedule.sat_sun_end_hour, minute=branch_schedule.sat_sun_end_min, second=0, microsecond=0)

    for j in range(30):
      interval = get_interval(add_minutes(current_day, 30*j))
      
      if lunch_start <= interval['dateTimeStart'] < lunch_end:
        continue

      if lunch_start < interval['dateTimeEnd'] <= lunch_end:
        continue

      if len(Appointment.objects.filter(pk=unit_id, datetime_start=interval['dateTimeStart'])) > 0:
        continue
      
      if interval['dateTimeEnd'] > day_end:
        break

      today_timeslots['timeSlots'].append(interval)
    if len(today_timeslots) > 0:
      result['availableTimeList'].append(today_timeslots)

  return JsonResponse(result)
