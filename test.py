from tkinter import Tk, Label, Entry, NSEW, Button


class BankApp(Tk):
    def __init__(self):
        super().__init__()
        card1_bank_lbl = Label(text=card1.bank)
        card2_bank_lbl = Label(text=card2.bank)
        card1_name_lbl = Label(text=card1.name)
        card2_name_lbl = Label(text=card2.name)
        card1_num_lbl = Label(text=card1.c_num)
        card2_num_lbl = Label(text=card2.c_num)
        card1_exp_lbl = Label(text=card1.expire)
        card2_exp_lbl = Label(text=card2.expire)
        self.card1_balance_lbl = Label(text=card1.balance)
        self.card2_balance_lbl = Label(text=card2.balance)

        self.card1_ent = Entry()
        self.card2_ent = Entry()
        add_btn = Button(text='Пополнить', command=self.add_coins)
        remove_btn = Button(text='Снять', command=self.remove_coins)
        move_btn = Button(text='Перевести')

        card1_bank_lbl.grid(row=0 , column=0 )
        card2_bank_lbl.grid(row=0 , column=1 )
        card1_name_lbl.grid(row=1 , column=0 )
        card2_name_lbl.grid(row=1 , column=1 )
        card1_num_lbl.grid(row=2 , column=0 )
        card2_num_lbl.grid(row=2 , column=1 )
        card1_exp_lbl.grid(row=3 , column=0 )
        card2_exp_lbl.grid(row=3 , column=1 )
        self.card1_balance_lbl.grid(row=4 , column=0 )
        self.card2_balance_lbl.grid(row=4 , column=1 )

        self.card1_ent.grid(row=5, column=0)
        self.card2_ent.grid(row=5, column=1)
        add_btn.grid(row=6, column=0, columnspan=2)
        remove_btn.grid(row=7, column=0, columnspan=2)
        move_btn.grid(row=8, column=0, columnspan=2)
        self.mainloop()

    def add_coins(self):
        m1 = int(self.card1_ent.get())
        m2 = int(self.card2_ent.get())
        card1.add_money(m1)
        card2.add_money(m2)
        self.card1_balance_lbl.configure(text=card1.balance)
        self.card2_balance_lbl.configure(text=card2.balance)

    def remove_coins(self):
        m1 = int(self.card1_ent.get())
        m2 = int(self.card2_ent.get())
        card1.remove_money(m1)
        card2.remove_money(m2)
        self.card1_balance_lbl.configure(text=card1.balance)
        self.card2_balance_lbl.configure(text=card2.balance)




class BankCard:
    def __init__(self, _bank, _name, _c_num, _expire):
        self.bank = _bank
        self.name = _name
        self.c_num = _c_num
        self.expire = _expire
        self.balance = 0
        self.pin = '123'

    def add_money(self, _amount):
        self.balance += _amount

    def remove_money(self, _amount):
        if _amount <= self.balance:
            self.balance -= _amount


card1 = BankCard('Т-банк', "Гавашелишвили Георгий",
                 "6309581530758861", "01-01-2036")
card2 = BankCard('Альфа', "Авдеев Андрей",
                 "8345184615409528","01-01-2036")

app = BankApp()