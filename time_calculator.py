def add_time(start, duration, start_day = ""):
  # New time string
  new_time = ""
  # Split start time into the time and AM/PM
  start_time = start.split()
  # Hour of the start time
  start_hour = int(start_time[0].split(":")[0])
  # Minute of the start time
  start_minute = int(start_time[0].split(":")[1])
  # AM/PM of the start time
  am_pm = start_time[1]

  # List of days of the week
  if start_day != "":
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_day = start_day.capitalize()
    start_day_number = days_of_week.index(start_day)
  
  # Absolute minutes of the start time
  if am_pm == "AM":
    start_abs_minutes = start_hour * 60 + start_minute
  else:
    start_abs_minutes = (start_hour+12) * 60 + start_minute
  
  # Hours of the duration
  duration_hour = int(duration.split(":")[0])
  # Minutes of the duration
  duration_minute = int(duration.split(":")[1])

  # Absolute minutes of the duration
  duration_abs_minutes = duration_hour * 60 + duration_minute
  
  # Number of days later
  days_later = (start_abs_minutes + duration_abs_minutes) // (24*60)

  # Calculation of the day of the new time
  if start_day != "":
    new_time_day = days_of_week[(start_day_number+days_later)%7]
  
  # AM/PM of the new time
  am_pm_flag_new_time = (start_abs_minutes + duration_abs_minutes) // (12*60) % 2

  # Defines if the new time is AM or PM
  if am_pm_flag_new_time == 0:
    am_pm_new_time = "AM"
  else:
    am_pm_new_time = "PM"
  
  # Calculate the new time
  new_minute = (start_minute + duration_minute)%60
  new_hour = (((start_hour + duration_hour + (start_minute + duration_minute)//60)-1)%12)+1

  # Format the new time
  if start_day != "":
    if days_later == 0:
      new_time = str(new_hour) + ":" + f'{new_minute:02d}' + " " + am_pm_new_time + ", " + new_time_day
    elif days_later == 1:
      new_time = str(new_hour) + ":" + f'{new_minute:02d}' + " " + am_pm_new_time + ", " + new_time_day + " (next day)"
    else:
      new_time = str(new_hour) + ":" + f'{new_minute:02d}' + " " + am_pm_new_time + ", " + new_time_day + " (" + str(days_later) + " days later)"
  else:
    if days_later == 0:
      new_time = str(new_hour) + ":" + f'{new_minute:02d}' + " " + am_pm_new_time
    elif days_later == 1:
      new_time = str(new_hour) + ":" + f'{new_minute:02d}' + " " + am_pm_new_time + " (next day)"
    else:
      new_time = str(new_hour) + ":" + f'{new_minute:02d}' + " " + am_pm_new_time + " (" + str(days_later) + " days later)"
  
  return new_time