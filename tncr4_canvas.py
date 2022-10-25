from tkinter import *
root=Tk()
root.title('canvas')
canvas_h=400
canvas_w=800
root.geometry(f"{canvas_w}x{canvas_h}")
can_widget=Canvas(root,width=canvas_w,height=canvas_h)
can_widget.pack()

can_widget.create_line(50,50,800,50,fill="blue")

can_widget.create_rectangle(50,50,400,300,fill="green")
can_widget.create_text(200,250, text="Bangladesh",font=("arial",20,'italic'))
can_widget.create_oval(140,120,260,230,fill="red")


root.mainloop()