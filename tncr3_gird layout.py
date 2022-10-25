from tkinter import *

def val():
    print(userv.get())
    print(passv.get())
    print(cont.get())
    print(serv.get())
    with open("record.csv","a") as k:
        k.write(f"\n{userv.get(),passv.get(),cont.get(),serv.get()}")



root=Tk()
root.geometry("800x450")
root.title("Tkinter project")

Label(text="Welcome to new Project",font=('Helvetica', 16, 'bold italic'),fg='black').grid(row=0,column=3,pady=15)

user= Label(root,text="Username")
passs=Label(root,text="Password")
contact=Label(root,text="Contact")
contact.grid(row=3)


user.grid(row=1)
passs.grid(row=2)

userv=StringVar()
passv=StringVar()
cont=StringVar()
serv=IntVar()


usere=Entry(root,textvariable= userv)
passe=Entry(root,textvariable= passv)
conte=Entry(root,textvariable=cont)


usere.grid(row=1,column=2)
passe.grid(row=2,column=2)
conte.grid(row=3,column=2)


Button(text="Submit",command=val).grid(row=5)

#chackbox
fserv=Checkbutton(text="Agree to all the term and Condition?",variable=serv)
fserv.grid(row=4,column=2)



#variable class in tkinter= BooleanVar, DoubleVar, IntVAr, StringVar

root.mainloop()