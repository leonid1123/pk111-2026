from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self):
        super().__init__()
        self.pic = PhotoImage(file='flag.png')
        for _row in range(0, 9):
            for _col in range(0, 9):
                tmp_btn = Button(self, image=self.pic)
                tmp_btn.bind('<Button-1>', self.btn_remove)
                tmp_btn.bind('<Button-3>', self.btn_mark)
                tmp_btn.grid(row=_row, column=_col)

    def btn_remove(self, event):
        print('левая кнопка')
        print(event)

    def btn_mark(self, event):
        print('правая кнопка')
        print(event)



app = App()
app.mainloop()