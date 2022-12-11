import sqlite3
import json
con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

def insert_operations():
  f = open('static/operations.json')
  data = json.load(f)
  for item in data:
    sql = f"insert into api_operation (type, description, duration, is_fast_area, is_normal_area, active) values ('{item['operationType']}', '{item['operationDescription']}', {item['durationMinutes']}, {item['isFastArea']}, {item['isNormalArea']}, {item['active']})"
    cur.execute(sql)
    con.commit()

def insert_branches():
  f = open('static/branches.json')
  data = json.load(f)
  for item in data:
    x = item['appointmentsSchedule']
    sql = f"insert into api_appointmentschedule (is_cashless, is_weekend_open, is_sunday_open, mon_fri_start_hour, mon_fri_start_min, mon_fri_end_hour, mon_fri_end_min, sat_sun_start_hour, sat_sun_start_min, sat_sun_end_hour, sat_sun_end_min, lunch_break_start_hour, lunch_break_start_min, lunch_break_end_hour, lunch_break_end_min) values ({x['isCashless']}, {x['isWeekendOpen']}, {x['isSundayOpen']}, {x['scheduleMonFriStart']['hour']}, {x['scheduleMonFriStart']['minute']}, {x['scheduleMonFriEnd']['hour']}, {x['scheduleMonFriEnd']['minute']}, {x['scheduleSatSunStart']['hour']}, {x['scheduleSatSunStart']['minute']}, {x['scheduleSatSunEnd']['hour']}, {x['scheduleSatSunEnd']['minute']}, {x['lunchBreakStart']['hour']}, {x['lunchBreakStart']['minute']}, {x['lunchBreakEnd']['hour']}, {x['lunchBreakEnd']['minute']})"
    res = cur.execute(sql)
    as_id = res.lastrowid
    euro_available = False
    try:
      euro_available = item['mfm_euro_available']
    except:
      euro_available = False

    euro_work_hours = False
    try:
      euro_work_hours = item['mfm_euro_work_hours']
    except:
      euro_work_hours = False

    euro_all_day = False
    try:
      euro_all_day = item['mfm_euro_all_day']
    except:
      euro_all_day = False

    
    
    sql2 = f"insert into api_branch (name, street, city, telephone, mfm_euro_available, mfm_euro_work_hours, mfm_euro_all_day, latitude, longitude, appointment_schedule_id) values ('{item['brn']}', '{item['br_street']}', '{item['br_city']}', '{item['telephone'][0]}', {euro_available}, {euro_work_hours}, {euro_all_day}, {float(item['location']['latitude'])}, {float(item['location']['longitude'])}, {as_id})"
    cur.execute(sql2)
    con.commit()

insert_branches()
