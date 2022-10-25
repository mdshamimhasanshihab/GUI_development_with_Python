from tkinter import *
root=Tk()
root.geometry("850x400")
root.title("Scroll bar")

# For connecting scroll bar to a widget
#1.widget (vscrollcommand=scrollbar.set)
#2.scrollbar.config(command=widget,yview)

scb=Scrollbar(root)
scb.pack(fill=Y,side=RIGHT)

lsb=Listbox(root)
for i in range(1,351):
    lsb.insert(END,f"item-{i}")
lsb.pack(fill=BOTH)



scb.config(command=lsb.yview)


root.mainloop()