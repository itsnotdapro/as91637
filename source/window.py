# Connect $4
# 17/05/18
# window.py

import tkinter as tk


class Window(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        canvas = tk.Canvas(width=800, highlightthickness=0, relief='ridge')
        canvas.place(x=0, y=0) # Header canvas

        self.header = tk.PhotoImage(file = "source/img/header.gif")
        canvas.create_image(0, 0, image = self.header, anchor="nw") # Add header image to canvas

        board_back = tk.Canvas(width = 640, height = 480) # Back canvas behind playing board makes a black outline
        board_back.place(x = 10, y = 135)
        board_back.create_rectangle(0, 64, 577, 437, fill = "black")

        self.board = tk.Frame(board_back, bg="black") # Playing area
        board_back.create_window((3, 3), window = self.board, anchor='nw')

        self.blank = tk.PhotoImage(file = "source/img/blank.gif") # Placeholder

        self.grid = [[],[],[],[],[],[],[]] # Each space on the board is held on this grid as a (y, x) value
        for y in range(7):
            for x in range(7):
                self.grid[y].append(tk.Canvas(self.board,
                                              width = 80,
                                              height = 60,
                                              highlightthickness=1,
                                              highlightbackground="black",
                                              relief='flat')) # Add a new space on board for current (y, x)

                self.grid[y][x].create_image(0, 0, image = self.blank, anchor='nw') # Add placeholder
                self.grid[y][x].grid(row = y, column = x)
