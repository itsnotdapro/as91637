# Connect $4
# 17/05/18
# window.py

import tkinter as tk
from logic import Game, Player
import sqlite3


class Window(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.player1 = Player("Playerholder", 420)
        self.player2 = Player("Computer", 420)

        # Image Decleration
        self.blank = tk.PhotoImage(file = "source/img/placeholdergrey.gif") # Placeholder
        self.orange = tk.PhotoImage(file = "source/img/orangegrey.gif") # Orange Counter
        self.red = tk.PhotoImage(file = "source/img/redgray.gif") # Red Counter
        self.show = tk.PhotoImage(file = "source/img/show.gif") # Top Button
        self.showred = tk.PhotoImage(file = "source/img/showred.gif") # Red Top Button
        self.showorange = tk.PhotoImage(file = "source/img/showorange.gif") # Orange Top Button
        self.header = tk.PhotoImage(file = "source/img/header.gif") # Header

        self.game = Game(player1, player2)

        canvas = tk.Canvas(width=800, highlightthickness=0, relief='ridge')
        canvas.create_image(0, 0, image = self.header, anchor="nw") # Add header image to canvas
        canvas.place(x=0, y=0) # Header canvas

        ## CREATE POOL ##
        self.pool = tk.Canvas(width = 170, height = 150)
        self.round_rectangle(self.pool, 4, 4, 170, 150, r=10, fill="black")
        self.round_rectangle(self.pool, 9, 9, 165, 145, r=10, fill="#777777")
        self.pool.place(x=600, y=170)
        self.poolframe = tk.Frame(bg = "#777777")
        tk.Label(self.poolframe, text="POOL", bg = "#777777", font=("Verdana", 25, "bold")).pack()
        self.poollabel = tk.Label(self.poolframe, bg = "#777777", text=("$" + str(self.game.pool)), font=("Verdana", 12)).pack(pady=20)
        self.pool.create_window((85, 25), window = self.poolframe, anchor = 'n')

        ## CREATE PLAYER 1 INFO ##
        self.player1info = tk.Canvas(width = 170, height = 150)
        self.round_rectangle(self.player1info, 4, 4, 170, 100, r=10, fill="#7F2A00")
        self.round_rectangle(self.player1info, 7, 7, 167, 97, r=10, fill="#FF5300")
        self.player1info.place(x=600, y=330)
        self.player1frame = tk.Frame(bg = "#FF5300")
        self.player1name = tk.Label(self.player1frame, bg="#FF5300", text="player1")
        self.player1name.pack()
        self.player1cash = tk.Label(self.player1frame, bg="#FF5300", text="$0")
        self.player1cash.pack()
        self.player1info.create_window((85, 25), window = self.player1frame, anchor = 'n')

        ## CREATE PLAYER 1 INFO ##
        self.player2info = tk.Canvas(width = 170, height = 150)
        self.round_rectangle(self.player2info, 4, 4, 170, 100, r=10, fill="#650400")
        self.round_rectangle(self.player2info, 7, 7, 167, 97, r=10, fill="#FF0900")
        self.player2info.place(x=600, y=445)
        self.player2frame = tk.Frame(bg = "#FF0900")
        self.player2name = tk.Label(self.player2frame, bg="#FF0900", text="player2")
        self.player2name.pack()
        self.player2cash = tk.Label(self.player2frame, bg="#FF0900", text="$0")
        self.player2cash.pack()
        self.player2info.create_window((85, 25), window = self.player2frame, anchor = 'n')

        board_back = tk.Canvas(width = 570, height = 480) # Back canvas behind playing board makes a black outline
        board_back.place(x = 10, y = 115)
        board_back.create_rectangle(0, 59, 570, 432, fill = "black")

        self.board = tk.Frame(board_back) # Playing area
        board_back.create_window((3, 0), window = self.board, anchor='nw')

        self.grid = [[],[],[],[],[],[],[]] # Each space on the board is held on this grid as a (y, x) value
        for y in range(7):
            for x in range(7):
                if y == 0: thick = 0
                else: thick = 1
                self.grid[y].append(tk.Canvas(self.board,
                                              width = 79,
                                              height = 60,
                                              highlightthickness=thick,
                                              highlightbackground="black",
                                              relief='sunken')) # Add a new space on board for current (y, x)

                if y == 0:
                    self.grid[y][x].create_image(0, 0, image = self.show, anchor='nw') # Add top buttons
                    self.grid[y][x].bind("<Enter>", self.change_on_enter) # Change image on cursor hover enter
                    self.grid[y][x].bind("<Leave>", self.change_on_leave) # Change image on cursor hover leave
                else: self.grid[y][x].create_image(0, 1, image = self.blank, anchor='nw') # Add placeholder
                self.grid[y][x].grid(row = y, column = x)

    ## END OF INITILISATION ##

        self.disable()

    def play(self):

        self.game.turn *= -1

    def change_on_enter(self, event):
        if self.game.turn == 1: event.widget.create_image(0, 0, image = self.showorange, anchor='nw')
        if self.game.turn == -1: event.widget.create_image(0, 0, image = self.showred, anchor='nw')

    def change_on_leave(self, event): event.widget.create_image(0, 0, image = self.show, anchor='nw')

    def disable(self):
        self.disableframe = tk.Canvas(width=590, height = 450, bg="black")
        self.disableframe.create_text(300, 230, fill="white", text="New Game", font=("Verdana", 27, "bold"))
        self.disableframe.place(x = 0, y = 110)

    def round_rectangle(self, canvas, x1, y1, x2, y2, r=25, **kwargs): # Thanks to SneakyTurtle on stackoverflow for this one.
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        canvas.create_polygon(points, **kwargs, smooth=True)
