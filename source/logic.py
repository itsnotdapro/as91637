# Connect $4
# 17/05/18
# logic.py

import itertools as iterate
from random import randint as rand

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.turn = 1 # 1 == orange, -1 == red
        self.pool = 0

        self.board = [[],[],[],[],[],[]]
        for y in range(6):
            for x in range(7): self.board[y].append(0)

    def play(self, space): # will return true if play was succesfull
        if self.turn == -1 and self.player2.name == "Computer": space = self.ai_play()
        for i, item in reversed(list(enumerate(self.board))):
            print(i, item)
            if item[space] == 0:
                self.board[i][space] = self.turn
                if self.turn == 1: self.player1.cash -= 10
                if self.turn == -1: self.player2.cash -= 10
                self.pool += 10
                return True
            continue
        return False

    def ai_play(self):

        for col in self.board:
            for i in col:
                margin = rand(-1, 1)
                if i == self.turn: return i + margin
        return rand(0, 6)

    def check(self):
        # set the hor and ver values
        for i in range(4):
            if i == 0: hor, ver = 0, 4
            if i == 1: hor, ver = 4, 0
            if i == 2: hor, ver = 4, 4

            # beign logic
            for y in range(6):
                for x in range(7):
                    if self.board[y][x] == self.turn: # check current space is set to the player's number
                        try:
                            # iter with a, b being the additives to the currently checked xy point on the table
                            for a, b in iterate.zip_longest(range(0, ver), range(0, hor)):
                                 # set a/b to 0 if the iter returns None as their values. This allows them to remain 0
                                # as the other value iterates
                                if a == None: a = 0
                                if b == None: b = 0
                                if i == 3: b = -b
                                if self.board[y+a][x+b] == self.turn: continue # check if xy point + ab is the players value
                                else: raise IndexError # if not then raise IndexError, effectivly skipping to next value
                            return True# else return True
                        except IndexError: continue # if run to end of table, move to next value
        return False # if all values are checked, and not returned True, return False


class Player:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
