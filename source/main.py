# Connect $4
# 17/05/18
# main.py

from tkinter import Tk
from window import Window
import sqlite3

def run(name):
    db = sqlite3.connect('source/data/playertable')
    cursor = db.cursor()
    cursor.execute('SELECT name, cash FROM players')
    data = cursor.fetchall()
    print(data)
    db.commit()
    db.close()

    root = Tk()
    root.title(name)
    root.resizable(False, False)
    root.tk_setPalette(background="#eeeeee")
    root.geometry("800x565")

    app = Window(root)

    root.mainloop()
