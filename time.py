import time as T
import calendar


x = T.time()

print(x)


# Getting current time

localtime = T.localtime(T.time())

# print(localtime)

"""
    Getting formatted time
    You can format any time as per your requirement, but simple method to get time in readable format is asctime() −
"""
"""
    Getting calendar for a month
    The calendar module gives a wide range of methods to play with yearly and monthly calendars. Here, we print a calendar for a given month ( Jan 2008 ) −
"""
cal = calendar.month(2022, 3)
# print(cal)

# Sleep Time method
# time.sleep(seconds) # 1,2,3,4,5

print("printing one")
T.sleep(5)
print("printing two")
