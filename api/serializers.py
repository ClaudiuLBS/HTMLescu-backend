from rest_framework import serializers
from .models import Appointment, Branch, AppointmentSchedule


class AppointmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Appointment
    fields = ('__all__')

class ScheduleSerializer(serializers.ModelSerializer):
  class Meta:
    model = AppointmentSchedule
    fields = ('__all__')

class BranchSerializer(serializers.ModelSerializer):
  appointment_schedule = ScheduleSerializer(required=True)
  class Meta:
    model = Branch
    fields = ('id', 'name', 'street', 'city', 'telephone', 'mfm_euro_available', 'mfm_euro_work_hours', 'mfm_euro_all_day', 'latitude', 'longitude', 'appointment_schedule')

