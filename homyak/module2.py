from tkinter import (Tk, Button, Entry,
                     Listbox, Variable, Label,
                     PhotoImage, NSEW)


class Homyak:
    def __init__(self):
        self.h_clicks = 0
        self.root = Tk()
        self.root.geometry('400x500+100+100')
        self.root.resizable(False,False)
        hom1 = PhotoImage(file='1.png')
        self.hom2 = PhotoImage(file='2.png')
        self.hom3 = PhotoImage(file='3.png')
        self.hom_lbl = Label(self.root, image=hom1)
        self.clicks_lbl = Label(text='Кликов: ')
        btn = Button(text='Жми!!!')
        btn.bind("<Button-1>", self.hom_click)
        exchange_btn = Button(text='Обмен кликов на ХомКоины')
        exchange_btn.bind("<Button-1>", self.exchange)
        self.hom_lbl.grid(row=0, column=0, columnspan=2)
        self.clicks_lbl.grid(row=1, column=0)
        exchange_btn.grid(row=1, column=1, sticky=NSEW,
                          pady=4)
        btn.grid(row=2, column=0,
                 columnspan=2, sticky=NSEW,
                 pady=10)


        self.root.mainloop()

    def hom_click(self, p1):
        self.h_clicks += 1
        self.clicks_lbl.configure(text=f"Кликов: {self.h_clicks}")
        if self.h_clicks >= 200:
            self.hom_lbl.configure(image=self.hom2)
        elif self.h_clicks >= 400:
            self.hom_lbl.configure(image=self.hom3)

    def exchange(self, p1):
        self.root.geometry('600x500+100+100')
        ex_clc_lbl = Label(text=f'Кликов: {self.h_clicks}')
        ex_homCoins_lbl = Label(text=f'ХомКоинов: {self.h_clicks//10}')
        ex_btn = Button(text='100 кликов в 10 ХомКоинов')
        shop_double = Button(text='Даблклик [200 Хк]')
        shop_avto = Button(text='Автоклик [50 Хк]')
        shop_super_avto = Button(text='Супер Автоклик [500 Хк]')
        shop20_100 = Button(text='20Хк за 100 кликов [50 Хк]')
        shop_rnd = Button(text='РаНдОм!!!')
        ex_clc_lbl.place(x=420, y=20)
        ex_homCoins_lbl.place(x=420, y=40)
        ex_btn.place(x=420, y=70)
        shop_double.place(x=420, y=200)
        shop_avto.place(x=420, y=240)
        shop_super_avto.place(x=420, y=280)
        shop20_100.place(x=420, y=320)
        shop_rnd.place(x=420, y=360)


app = Homyak()
