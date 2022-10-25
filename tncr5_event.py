from tkinter import *

def harry(event):
    print(f"Yoy clicked at{event.x},{event.y}")
root=Tk()
root.title('event')
canvas_h=400
canvas_w=800
root.geometry(f"{canvas_w}x{canvas_h}")
widget=Button(root,text="Click me")
widget.grid()

widget.bind('<Button-1>',harry)
widget.bind("<Double-1>",quit)





root.mainloop()