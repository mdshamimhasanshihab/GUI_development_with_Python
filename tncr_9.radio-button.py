from tkinter import *
import tkinter.messagebox as tmsg

def order():
    a = tmsg.showinfo('MSG', f"We have received your order {var.get()}")
    with open("record2.txt","a") as k:
        k.write(f"\n{var.get()}")


root=Tk()
root.geometry("850x400")
root.title("Radio Button")
f2=Frame(root,bg='black',borderwidth=2,relief=SUNKEN)
f2.pack(anchor='nw')
var=IntVar()
var.set(1)
#Label(root,text="What would you like to have?",pady=15,font="lucida 20 bold").pack(anchor='nw')
Radiobutton(f2,text="dosa",variable=var).pack(anchor='nw')
radio=Radiobutton(root,text="porota",variable=var,value=2).pack(anchor='nw')
radio=Radiobutton(root,text="puri",variable=var,value=3).pack(anchor='nw')

itm_list=["dosa","alu puri","pani puri"]
for i,item in enumerate(itm_list):
    radio=Radiobutton(root,text=item,variable=var,value=i+1).pack(anchor='nw')

Button(root,text="order now",command=order).pack()




root.mainloop()