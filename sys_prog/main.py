import os

from tkinter import (Tk, Variable, Listbox,
                     Button, Label, NSEW)


def get_files(path):
    all_files.clear()
    all_dirs.clear()
    res = os.scandir(path)
    for item in res:
        if item.is_dir():
            all_dirs.append(item.name)
        if item.is_file():
            all_files.append(item.name)
    files_var.set(all_files)
    dirs_var.set(all_dirs)

def lst_click(p1):
    print(dirs_view.selection_get())
    get_files(path + '/' + dirs_view.selection_get())

win = Tk()
win.geometry("600x300+100+100")
win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)
all_files = []
all_dirs = []
files_var = Variable(value=all_files)
dirs_var = Variable(value=all_dirs)
files_view = Listbox(listvariable=files_var)
dirs_view = Listbox(listvariable=dirs_var)
dirs_view.bind('<Double-Button-1>',lst_click)
files_view.grid(row=0, column=0, sticky=NSEW)
dirs_view.grid(row=0, column=1, sticky=NSEW)

path = 'C:/Users/Leo/Documents/pk111'
get_files(path)
win.mainloop()

