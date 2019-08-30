import datetime as dt
import os

hrs = int(input("Hrs- "))
min = int(input("Min- "))

count = 0
while(1):
    nhr = dt.datetime.now().hour
    nmin = dt.datetime.now().minute
    if (nhr > 12):
        nhr = nhr - 12
    if hrs == nhr and min == nmin:
        count=1
        break
if count==1:
    os.system("sample.mp3")
    exit(0)








