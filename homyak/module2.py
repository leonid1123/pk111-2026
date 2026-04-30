from tkinter import (Tk, Button, Entry,
                    Listbox, Variable, Label,
                    PhotoImage)

class Homyak:
    def __init__(self):
        self.h_clicks = 0
        root = Tk()
        hom1 = PhotoImage(file='1.png')
        self.hom2 = PhotoImage(file='2.png')
        hom3 = PhotoImage(file='3.png')
        self.hom_lbl = Label(root,image=hom1)
        self.clicks_lbl = Label(text='Кликов: ')
        btn = Button(text='Жми!!!')
        btn.bind("<Button-1>", self.hom_click)
        self.hom_lbl.grid(row=0, column=0)
        self.clicks_lbl.grid(row=1, column=0)
        btn.grid(row=2, column=0)

        root.mainloop()

    def hom_click(self, p1):
        self.h_clicks += 1
        self.clicks_lbl.configure(text=f"Кликов: {self.h_clicks}")
        if self.h_clicks >= 2:
            self.hom_lbl.configure(image=self.hom2 )


app = Homyak()
