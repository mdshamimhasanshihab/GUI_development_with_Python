from tkinter import *


def myf():
    print('I am working')



root=Tk()
root.geometry("850x400")
root.title("menu and submenu")


#this task is made to create menu bar
#my_menu=Menu(root)
#my_menu.add_command(label='file',command=myf)
#my_menu.add_command(label="exit",command=quit)
#root.config(menu=my_menu)


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




root.mainloop()