# 10. Write a python script to display the current date and time. First create variables to store date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM. Hint for solution is also available as screenshot.

from datetime import datetime
date=datetime.today()
print(date)

d1=date.strftime("%d-%m-%Y and %I:%M %p")
print(d1)

d1=date.strftime("%B %d %Y")
print(d1)

d1=date.strftime("%d/%b/%Y")
print(d1)

d1=date.strftime("%H:%M:%S")#railway time
print(d1)

d1=date.strftime("%d-%m-%y")
print(d1)