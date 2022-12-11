from django.db import models

class AppointmentSchedule(models.Model):
  is_cashless = models.BooleanField()
  is_weekend_open = models.BooleanField()
  is_sunday_open = models.BooleanField()
  mon_fri_start_hour = models.IntegerField()
  mon_fri_start_min = models.IntegerField()
  mon_fri_end_hour = models.IntegerField()
  mon_fri_end_min = models.IntegerField()
  sat_sun_start_hour = models.IntegerField()
  sat_sun_start_min = models.IntegerField()
  sat_sun_end_hour = models.IntegerField()
  sat_sun_end_min = models.IntegerField()
  lunch_break_start_hour = models.IntegerField()
  lunch_break_start_min = models.IntegerField()
  lunch_break_end_hour = models.IntegerField()
  lunch_break_end_min = models.IntegerField()


class Branch(models.Model):
  name = models.CharField(max_length=128)
  street = models.CharField(max_length=1024)
  city = models.CharField(max_length=128)
  telephone = models.CharField(max_length=20)
  mfm_euro_available = models.BooleanField()
  mfm_euro_work_hours = models.BooleanField()
  mfm_euro_all_day = models.BooleanField()
  latitude = models.FloatField()
  longitude = models.FloatField() 
  appointment_schedule = models.OneToOneField(AppointmentSchedule, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.name
  
class Appointment(models.Model):
  name = models.CharField(max_length=128, null=False)
  phone_number = models.CharField(max_length=15, null=True)
  email = models.EmailField(null=False)
  datetime_start = models.DateTimeField()
  branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
