from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("850x450")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.sbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w")
        self.sbar.pack(side=BOTTOM, fill=X)
    def click(self):
        print("Button click")

    def crtbutn(self,intxt):
        Button(self, text=intxt, command=self.click).pack()


if __name__ == '__main__':
    window=GUI()
    window.status()
    window.crtbutn("click me")
    window.mainloop()
