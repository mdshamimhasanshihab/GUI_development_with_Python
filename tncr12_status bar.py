from tkinter import *

def add():
    var.set("Busy")
    sbar.update()
    import time
    time.sleep(2)
    var.set("Ready Now")

root=Tk()
root.geometry("850x400")
root.title("Status Bar")

var=StringVar()
var.set("Ready")
sbar=Label(root,textvariable=var,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)

Button(root,text="Upload",command=add).pack()


root.mainloop()