import datetime as dt
import os

hrs = int(input("Hrs- "))
min = int(input("Min- "))
getampm = input("AM/PM- ")
getampm = getampm.upper()

count = 0
while(1):
    nhr = dt.datetime.now().hour
    nmin = dt.datetime.now().minute
    temp = dt.datetime.now()
    store2 = temp.strftime("%p")
    osampm = store2[-2:]
    if getampm == osampm:
        if (nhr > 12):
            nhr = nhr - 12
        if hrs == nhr and min == nmin:
            count=1
            break
if count==1:
    os.system("sample.mp3")
    exit(0)