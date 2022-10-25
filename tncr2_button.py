from tkinter import *
def hello():
    print("Button is working")
def name():
    print("Md Shamim Hasan")
def id():
    print("201936032")
root=Tk()
root.geometry("800x450")
frame=(Frame(root,borderwidth=8,bg="grey",relief=SUNKEN))
frame.pack(side=LEFT,anchor='nw')
b1=Button(frame,fg='red',text="button 1",command=hello)
b1.pack(side=LEFT)
b2=Button(frame,fg='red',text="button 2",command=name)
b2.pack(side=LEFT)
b3=Button(frame,fg='red',text="button 3",command=id)
b3.pack(side=LEFT)
root.mainloop()