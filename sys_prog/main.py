import os

from tkinter import (Tk, Variable, Listbox,
                      Button, Label, NSEW, W)

class SysProgOOP:
    def __init__(self):
        self.path = 'C:/Users/Leo/Documents/pk111'
        win = Tk()
        win.geometry("600x300+100+100")
        win.grid_columnconfigure(0, weight=1)
        win.grid_columnconfigure(1, weight=1)
        self.all_files = []
        self.all_dirs = []
        self.files_var = Variable(value=self.all_files)
        self.dirs_var = Variable(value=self.all_dirs)
        self.files_view = Listbox(listvariable=self.files_var)
        self.dirs_view = Listbox(listvariable=self.dirs_var)
        up_btn = Button(text='UP')
        up_btn.bind('<Button-1>', self.go_up)
        self.dirs_view.bind('<Double-Button-1>', self.lst_click)
        up_btn.grid(row=0, column=1, sticky=W)
        self.files_view.grid(row=1, column=0, sticky=NSEW)
        self.dirs_view.grid(row=1, column=1, sticky=NSEW)

    def show_files_dirs(self):
        self.all_files.clear()
        self.all_dirs.clear()
        res = os.scandir(self.path)
        for item in res:
            if item.is_dir():
                self.all_dirs.append(item.name)
            if item.is_file():
                self.all_files.append(item.name)
        self.files_var.set(self.all_files)
        self.dirs_var.set(self.all_dirs)

    def path_change(self):
        new_dir = self.dirs_view.selection_get()
        self.path = self.path + '/' + new_dir
        self.show_files_dirs()

app = SysProgOOP()


# def get_files(path):
#     all_files.clear()
#     all_dirs.clear()
#     res = os.scandir(path)
#     for item in res:
#         if item.is_dir():
#             all_dirs.append(item.name)
#         if item.is_file():
#             all_files.append(item.name)
#     files_var.set(all_files)
#     dirs_var.set(all_dirs)
#
#
# def lst_click(p1):
#     print(dirs_view.selection_get())
#     path = path + '/' + dirs_view.selection_get()
#     get_files(path)
#
# def up_dir(p1):
#
#
# win = Tk()
# win.geometry("600x300+100+100")
# win.grid_columnconfigure(0, weight=1)
# win.grid_columnconfigure(1, weight=1)
# all_files = []
# all_dirs = []
# files_var = Variable(value=all_files)
# dirs_var = Variable(value=all_dirs)
# files_view = Listbox(listvariable=files_var)
# dirs_view = Listbox(listvariable=dirs_var)
# up_btn = Button(text='UP')
# dirs_view.bind('<Double-Button-1>', lst_click)
# up_btn.grid(row=0, column=1, sticky=W)
# files_view.grid(row=1, column=0, sticky=NSEW)
# dirs_view.grid(row=1, column=1, sticky=NSEW)
#
# path = 'C:/Users/Leo/Documents/pk111'
# get_files(path)
# win.mainloop()
#
