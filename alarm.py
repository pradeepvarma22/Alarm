import datetime as dt
import os
from tkinter import *
def gui_screen():
    root = Tk()
    root.title("Alarm")
    root.geometry("500x400")
    heading = Label(root,text="WakeUp",font=("arial",40,"bold"),fg="steelblue").pack()
    label1 = Label(root,text="Hrs",font=("arial",15,"bold")).place(x=8,y=150)
    nhrs = int()
    entry_box=Entry(root,textvariable=hrs,width=5).place(x=8,y=180)

    label2 = Label(root, text="Min", font=("arial", 15, "bold")).place(x=9, y=220)
    nmin = int()
    entry_box = Entry(root, textvariable=hrs, width=5).place(x=10, y=250)

    



    root.mainloop()


gui_screen()
#hrs = int(input("Hrs- "))
#min = int(input("Min- "))

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







