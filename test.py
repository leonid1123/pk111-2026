from tkinter import (Tk, Button,
                     Listbox,Entry,NSEW,
                     Variable)
import pymysql.cursors


class App(Tk):
    def __init__(self):
        super().__init__()
        self.messages = []
        self.msg_var = Variable(value=self.messages)
        self.view = Listbox(listvariable=self.msg_var)
        self.msg_ent = Entry()
        self.get_msg = Button(text='Получить сообщения', command=self.get_msg_m)
        self.send_msg = Button(text='Отправить', command=self.send_msg)
        self.geometry("400x300")
        self.columnconfigure(0, weight=1)
        self.get_msg.grid(row=0, column=0, sticky=NSEW)
        self.view.grid(row=1, column=0, sticky=NSEW)
        self.msg_ent.grid(row=2, column=0, sticky=NSEW)
        self.send_msg.grid(row=3, column=0, sticky=NSEW)
        self.conn = pymysql.connect(host="192.168.1.61",
                                    user='pk111',
                                    password='1234',
                                    database='pk_111')
        self.cursor = self.conn.cursor()
        self.mainloop()

    def get_msg_m(self):
        self.cursor.execute('SELECT * FROM msg')
        ans = self.cursor.fetchall()
        self.messages = []
        for item in ans:
            self.messages.append(f"{item[2]}:{item[3]} {item[1]}")
        self.msg_var.set(self.messages)

    def send_msg(self):
        my_msg = self.msg_ent.get()
        sql = 'INSERT INTO msg(user,msg) VALUES(%s,%s)'
        info = ('MEGANAGIBATOR8000', my_msg)
        self.cursor.execute(sql,info)
        self.conn.commit()
        self.get_msg_m()


app = App()