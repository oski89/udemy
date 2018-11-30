import datetime

t = datetime.time(5, 25, 1)
print(t)

today = datetime.date.today()
print(today)
print(today.timetuple())
print(today.day)
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)

d1 = datetime.date(2018, 11, 28)
print(d1)

d2 = d1.replace(year=1989)
print(d2)

print(d1-d2)
