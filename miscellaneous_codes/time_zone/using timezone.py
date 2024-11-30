import pytz
import datetime
print(pytz.all_timezones)
print(datetime.datetime.now(pytz.timezone('US/Pacific')))
print(datetime.datetime.now(pytz.timezone('US/Indiana-Starke')))