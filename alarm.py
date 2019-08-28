import datetime as dt
import os

hrs = int(input("Enter Time in Hrs- "))
#min = int(input("Enter Time in Min- "))

count = 0
while(1):
    nhr = dt.datetime.now().hour
    if (nhr > 12):
        nhr = nhr - 12
    if hrs == nhr:
        count=1
        break
if count==1:
    os.system("sample.mp3")
    exit(0)








