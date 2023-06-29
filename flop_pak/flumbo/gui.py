import tkinter as tk
from subprocess import call
def open_py_file():
    call (["python", "char.py"])
def open_py_file1():
    call (["python", "unlock.py"])
win = tk.Tk()
win.title("Flumbo Docs")
#Adds a title
title = tk.Label(win,text="Flumbo Docs",font=("sans-serif",60), fg = "Black" )
title.pack()
flum_char = tk.Button(win,text="Experments",font=("sans-serif",30), fg = "Black")
flum_char.pack()
flum_char.config(command=open_py_file)
flum_un = tk.Button(win,text="Unlock\nCommandLine",font=("sans-serif",30), fg = "Black")
flum_un.pack()
flum_un.config(command=open_py_file1)
win.mainloop()
