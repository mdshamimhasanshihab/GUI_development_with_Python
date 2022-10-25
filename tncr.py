from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.geometry("700x500")
root.minsize(500,300)
root.maxsize(1000,800)
root.title("Simple Calculator")
sha=Label(text="Do Your Calculation")
sha.pack()




#importing photo
pht=PhotoImage(file="001.png") #tkinter dont support jpg file.
phtt=Label(image=pht)
#phtt.pack()

#For jpg file..
img=Image.open("IMG_0565.png.JPG")
imgg=ImageTk.PhotoImage(img)

immg=Label(image=imgg)
#immg.pack()


#Advanced label
# text- to add text
#bd-background
#fg-foreground
#font-sets the font
#font=("comicsansms",12,'bold') or font="comicsansms 12 bold"
#padx-x padding
#pady-y padding
#relief-border styling-SUNKEN,RAISED,GROOVE,RIDGE

title_label=Label(text='''You can download free PNG images with transparent backgrounds from the
\n largest collection on Pngtree. With these PNG images,
\n you can directly use them in''',bg='grey',fg='white',padx=50,pady=50,font=("comicsansms",12,'bold'),borderwidth=3,relief=SUNKEN)

#important pack option
#title_label.pack(anchor='nw',side=TOP)
#title_label.pack(anchor='nw',side=TOP,fill=X)
title_label.pack(anchor='nw',side=TOP,fill=X)


title_label.pack()



root.mainloop()