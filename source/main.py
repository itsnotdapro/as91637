# Connect $4
# 17/05/18
# main.py

from tkinter import Tk
from window import Window

def run(name):
    root = Tk()
    root.title(name)
    root.resizable(False, False)
    root.tk_setPalette(background="#eeeeee")
    root.geometry("800x565")

    app = Window(root)

    root.mainloop()
