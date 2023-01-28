# Time calculator function
def time_calculator(part_of_the_day,
                    hour_1,
                    minute_1,
                    hour_2,
                    minute_2,
                    day=None):
  # Attributes
  list_of_days = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
    "Sunday"
  ]
  day_match_index = 0
  potd = ""  # Part of the day
  actual_day = ""

  # Convert data to minutes
  if (part_of_the_day == "PM"):
    m = (
      (12 + int(hour_1) + int(hour_2)) * 60) + (int(minute_1) + int(minute_2))
    h = (m - (m % 60)) / 60
    d = (h - (h % 24)) / 24
    m = (m % 60)
    h = (h % 24)
  else:
    m = ((int(hour_1) + int(hour_2)) * 60) + (int(minute_1) + int(minute_2))
    h = (m - (m % 60)) / 60
    d = (h - (h % 24)) / 24
    m = (m % 60)
    h = (h % 24)

  # Calculate POTD
  if 12 <= h < 13:
    potd = "PM"
  elif 1 <= h < 12:
    potd = "AM"
  elif 13 <= h < 24:
    potd = "PM"
    h -= 12
  elif 0 <= h < 1:
    potd = "AM"
    h += 12

  # Calculating the day transition
  if day is not None and d != 0:
    for index in range(0, len(list_of_days)):
      if list_of_days[index].lower() == day.lower():
        day_match_index = index
    actual_day = list_of_days[int((day_match_index + d) % 7)]
  elif day is not None and d == 0:
    for index in range(0, len(list_of_days)):
      if list_of_days[index].lower() == day.lower():
        day_match_index = index
    actual_day = list_of_days[int((day_match_index + d) % 7)]

  # Return the right time format
  if m < 10:
    m = f"0{m}"
  if day != None:
    if 1 < d:
      return f"{h:.0f}:{m} {potd}, {actual_day} ({d:.0f} days later)"
    elif d == 1:
      return f"{h:.0f}:{m} {potd}, {actual_day} (next day)"
    else:
      return f"{h:.0f}:{m} {potd}, {actual_day}"
  else:
    if 1 < d:
      return f"{h:.0f}:{m} {potd} ({d:.0f} days later)"
    elif d == 1:
      return f"{h:.0f}:{m} {potd} (next day)"
    else:
      return f"{h:.0f}:{m} {potd}"


# Add time function
def add_time(starting_time, added_time, current_day=None):
  # Creating the components from the given times
  starting_time = [x.split(':') for x in starting_time.split(' ')]
  added_time = added_time.split(':')

  # Return new time
  time = time_calculator(starting_time[1][0], starting_time[0][0],
                         starting_time[0][1], added_time[0], added_time[1],
                         current_day)
  return time
