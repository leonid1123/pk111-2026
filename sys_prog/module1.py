import os
from tkinter import (Tk, Button, Label,
Listbox, Variable)

def wlk_fun(par_1):
    ## сделать переход по папкам и открытие файлов
    res = os.walk("C:/Users/Leo/Documents/pk111")
    for a,b,c in res:
        print(os.listdir(a))

def get_files(par_1):
    fl = []
    dirs = []
    res = os.listdir("C:/Users/Leo/Documents/pk111")
    for item in res:
        point = item.find(".")
        if point != -1:
            fl.append(item)
        else:
            dirs.append(item)
    files_var.set(dirs + fl)


m_win = Tk()
path_lbl = Label(text="C:/Users/Leo/Documents/pk111")
path_lbl.grid(row=0, column=0)

files=["pup",'mup']
files_var = Variable(value=files)
files_view = Listbox(listvariable=files_var, width=90)
files_view.grid(row=1, column=0)

btn = Button(text='Получить список файлов')
btn.bind("<Button-1>", get_files)
btn.grid(row=2, column=0)

btn_walk = Button(text='WALK функция')
btn_walk.bind('<Button-1>', wlk_fun)
btn_walk.grid(row=3, column=0)

m_win.mainloop()


