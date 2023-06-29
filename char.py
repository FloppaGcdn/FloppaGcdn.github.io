import tkinter as tk
from subprocess import call
def open_py_file():
    call(["python", "charOOO2.py"])
win = tk.Tk()
win.title("Flumbo Experments")
title = tk.Label(win,text="Flumbo Experments",font=("sans-serif",60), fg = "Black" )
title.pack()
OOO1 = tk.Button(win,text="ID:0002",font=("sans-serif",30), fg = "Grey")
OOO1.config(command=open_py_file)
OOO1.pack()
win.mainloop()