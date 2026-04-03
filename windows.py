import tkinter
from tkinter import Tk, Button, Toplevel

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("200x200")
        self.btn = Button(text='Окно2', command=self.win2)
        self.btn.pack()
        self.mainloop()

    def win2(self):
        self.win_2 = tkinter.Toplevel()
        self.win_2.geometry("300x300")

app = App()
