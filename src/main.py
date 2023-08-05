from datetime import datetime
a = datetime.now()
day = 0
l = a.strftime("%Y" "," "%m" "," "%d")
present_time = l.split(",")
d = input("Enter your birthday Y/m/d: ")
birthday = d.split("/")
ptm = int(present_time[1])
ptd = int(present_time[2])
b = int(birthday[1])
bdm = b
bdd = int(birthday[2])
if bdd > ptd:
  day = day + (bdd - ptd)
else:
  day = day + ((bdd+30) - ptd)
  bdm = bdm - 1
if bdm > ptm:
  day = day + ((bdm - ptm) * 30)
else:
  day = day + (((bdm+12) - ptm) * 30)
if day > 350:
  day += 5
elif day > 240:
  day += 4
elif day > 120:
  day += 2
elif day > 60:
  day += 1
print(day)