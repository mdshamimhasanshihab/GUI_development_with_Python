from tkinter import *
import tkinter.messagebox as tmsg



def myf():
    print('I am working')

def help():
    print("i will help u")
    a=tmsg.showinfo('HELP','something is wrong')
def rate():
    x=tmsg.askquestion("Rate us"," was your experience good?")
    print(x)
    if x=="yes":
        msg="Great. Rate us on app store"
    else:
        msg="Tel us, What went wrong?"
    tmsg.showinfo("experience",msg)


root=Tk()
root.geometry("850x400")
root.title("menu and submenu")





mnb=Menu(root)
m1=Menu(mnb,tearoff=0)
m1.add_command(label='save',command=myf)
m1.add_command(label='save as',command=myf)
m1.add_command(label='print',command=myf)
m1.add_separator()
m1.add_command(label='exit',command=quit)

mnb.add_cascade(label='file',menu=m1)
root.config(menu=mnb)



m2=Menu(mnb,tearoff=0)
m2.add_command(label='cut',command=myf)
m2.add_command(label='copy',command=myf)
m2.add_command(label='paste',command=myf)
m2.add_separator()
m2.add_command(label='exit',command=quit)

mnb.add_cascade(label='edit',menu=m2)
root.config(menu=mnb)

m3=Menu(mnb,tearoff=0)
m3.add_command(label='help',command=help)
m3.add_command(label='Rate',command=rate)
mnb.add_cascade(label='Help',menu=m3)
root.config(menu=mnb)

root.mainloop()