import tkinter 
from tkinter import ttk
import sv_ttk

root = tkinter.Tk()

button = ttk.Button(root, text="wa")
button.pack()
sv_ttk.set_theme('dark')

root.mainloop()