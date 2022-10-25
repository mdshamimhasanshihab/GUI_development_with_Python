from tkinter import *
import tkinter.messagebox as tmsg

def getdollar():
    #print(f"we have credited {myslider2.get()} dollar to your bank account")
    a = tmsg.showinfo('MSG', f"You have rated {myslider2.get()} for our service.")
    with open("record2.txt","a") as k:
        k.write(f"\n{myslider2.get()}")



root=Tk()
root.geometry("850x400")
root.title("tkinter slider")


#myslider=Scale(root,from_=0,to=100)
#myslider.pack()
Label(root,text="Rate us plz").pack()

myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.set(50)
myslider2.pack()

Button(root,text="Submit",command=getdollar).pack()

root.mainloop()