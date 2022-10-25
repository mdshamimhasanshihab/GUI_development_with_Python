from tkinter import *
import tkinter.messagebox as tmsg

def add():

    lbx.insert(ACTIVE,input("inp:"))
    


i=0
root=Tk()
root.geometry("850x400")
root.title("List Box")

lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First item")
Button(root,text="Add Item",command=add).pack()



root.mainloop()