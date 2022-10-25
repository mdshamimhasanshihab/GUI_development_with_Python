from tkinter import *
root=Tk()
root.geometry('800x450')
f1=Frame(root,bg='grey',borderwidth=8,relief=SUNKEN)
f2=Frame(root,bg='grey',borderwidth=8,relief=SUNKEN)

f1.pack(side=LEFT,fill=Y)
f2.pack(side=TOP,fill=X)

l=Label(f1,text="Project Tkinter")
m=Label(f2,text='Pycharm Project',font=('Helvetica', 16, 'bold italic'),fg='red')

l.pack(fill = BOTH, expand = True)
m.pack(fill = BOTH, expand = True)

root.mainloop()