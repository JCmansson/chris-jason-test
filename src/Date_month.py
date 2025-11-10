from datetime import datetime
import calendar

date_iso = "2025-12-11"
date_time = datetime.strptime(date_iso, "%Y-%m-%d")
print(date_time)

# get month number
num = date_time.month
print('Month Number:', num)

# get month name
print('Month full name is:', calendar.month_name[num])
print('Month short name is:', calendar.month_abbr[num])