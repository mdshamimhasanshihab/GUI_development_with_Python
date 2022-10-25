from tkinter import *
root=Tk()
root.geometry("655x444")
root.title("Tips & Tricks")
root.wm_iconbitmap("1.ico")
root.configure(background="light blue")

w=root.winfo_screenwidth()
h=root.winfo_screenheight()
print(f"{w}x{h}")



root.mainloop()