import datetime as dt

a = dt.datetime.now()

# print(a)
# print("date=",a.date())
# print("time=",a.time())
# convert to date string
# print(a.strftime("%d/%m/%y"))

# convert to time string
# print(a.strftime("%H:%M:%S"))

# year
# print(a.strftime("%y"))
# four digit
# print(a.strftime("%Y"))

# month
# print(a.strftime("%m"))
# day
# print(a.strftime("%d"))

# fullname of weekday
print(a.strftime("%A"))

# three char of weekday
print(a.strftime("%a"))

# month
print(a.strftime("%B")) # full month name
print(a.strftime("%b")) # three char of month

# hour
print(a.strftime("%H")) # 24 hour format
print(a.strftime("%I")) # 12 hour format

# find microsecond
print(a.strftime("%f"))

# am/pm format
print(a.strftime("%p"))

# local return data/time
print(a.strftime("%c"))
print(a.strftime("%X")) # time
print(a.strftime("%x")) # date

# return utc offset
print(a.strftime("%z"))
print(a.strftime("%Z")) # time zone

# return day of the year
print(a.strftime("%j"))

# return day of the number in decimal(0-sunday, 6-saturday)
print(a.strftime("%w"))

print("Time in 24 hours format:", a.strftime("%H-%M-%S"))
print("Time in 12 hours format:", a.strftime("%I-%M-%S"))

# return microsecond
print(a.strftime("%f"))
print(a.strftime("%p"))

