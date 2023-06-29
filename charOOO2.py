import tkinter as tk

win = tk.Tk()
win.title("Flumbo Experments")
title = tk.Label(win,text="ID:0002",font=("sans-serif",60), fg = "Black")
title.pack()
Name = tk.Label(win,text="Alias:The Creature",font=("sans-serif", 30), fg = "Black")
Name.pack()
Genome = tk.Label(win,text="Genomes:Human, Flumium",font=("sans-serif", 10), fg = "Black")
Genome.pack()
Case = tk.Label(win,text="Case update: 1\n\nThe Creature was very confused when he was fist alive",font=("sans-serif", 20), fg = "Black")
Case.pack()
win.mainloop()
