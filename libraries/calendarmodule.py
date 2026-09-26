import calendar
# leapyear = calendar.isleap(2024)
# print(leapyear)

# x =calendar.calendar(2024, w = 1, l = 1, c= 6, m = 3)
# print(x)
'''
year: The year to display.
w: Width of date columns.
l: Number of lines for each week.
c: Number of spaces between month columns.
m: Number of months per row.
'''
# months_leap = calendar.leapdays(2000, 2024)
# print(months_leap)

# month = calendar.month(2024, 9, w =1, l = 1)
# print(month)

# month = calendar.monthcalendar(2024, 9) #returns the matrix of the calenadar
# print(month)

# month = calendar.monthrange(2024, 8)
# print(month)

day = calendar.weekday(2024, 8, 1)
print(day)