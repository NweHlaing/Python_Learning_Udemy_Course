import datetime

t = datetime.time(4, 20, 1)
today = datetime.date.today()
print(today)


# Let's show the different components
print(t)
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)