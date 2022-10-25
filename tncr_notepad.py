from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os



root=Tk()
root.geometry("500x400")

root.title("Note Pad")
#root.wm_iconbitmap("1.ico")
root.configure(background="light blue")


TextArea=Text(root,font="lucida 13")
file=None
TextArea.pack(expand=True,fill=BOTH)



def newf():
    global file
    root.title("untitled-notepad")
    file=None
    TextArea.delete(1.0,END)


def savef():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt" ,filetypes=[('All Files','*.*'),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + "-Notepad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()




def openf():
    global file
    file=askopenfilename(defaultextension=".txt",
                         filetypes=[('All Files','*.*'),("Text Documents","*.txt")])

    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        TextArea.delete(1.0,END)
        f1=open(file,'r')
        TextArea.insert(1.0,f1.read())
        f1.close()

def save_as():
    global file
    file = asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt",
                             filetypes=[('All Files', '*.*'), ("Text Documents", "*.txt")])
    print(file)
    if file == "":
        file = None
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + "-Notepad")


def printf():
    messagebox.showinfo('Attention!!', 'First connect with an printer, carefully.')



def cutf():
    TextArea.event_generate(("<<Cut>>"))
    input = TextArea.get(1.0, END)
    print(input)
def copyf():
    TextArea.event_generate(("<<Copy>>"))

def pastef():
    TextArea.event_generate(("<<Paste>>"))
def select_all():
    pass
def helpf():
    messagebox.showinfo('HELP', 'Developer will help you')

def ratef():
    messagebox.askquestion("Rate us"," was your experience good?")



def myf():
    print('I am working')




mnb=Menu(root)
m1=Menu(mnb,tearoff=0)
m1.add_command(label='new',command=newf)
m1.add_command(label='save',command=savef)
m1.add_command(label='open',command=openf)
m1.add_command(label='save as',command=save_as)
m1.add_command(label='print',command=printf)
m1.add_separator()
m1.add_command(label='exit',command=quit)
mnb.add_cascade(label='file',menu=m1) #file er vitor rakhar jonno
root.config(menu=mnb)





m2=Menu(mnb,tearoff=0)
m2.add_command(label='cut',command=cutf)
m2.add_command(label='copy',command=copyf)
m2.add_command(label='paste',command=pastef)
m2.add_command(label='select all',command=select_all)
m2.add_separator()
m2.add_command(label='delete',command=quit)
mnb.add_cascade(label='edit',menu=m2) #file er vitor rakhar jonno
root.config(menu=mnb)


m3=Menu(mnb,tearoff=0)
m3.add_command(label='help',command=helpf)
m3.add_command(label='Rate',command=ratef)
mnb.add_cascade(label='Help',menu=m3)
root.config(menu=mnb)



#Adding scrollbar


scb=Scrollbar(TextArea)
scb.pack(fill=Y,side=RIGHT)
scb.config(command=TextArea.yview)
TextArea.config(yscrollcommand=scb.set)

root.mainloop()