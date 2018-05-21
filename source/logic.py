# Connect $4
# 17/05/18
# logic.py


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.turn = 1 # 1 == orange, -1 == red
        self.pool = 0

        self.board = [[],[],[],[],[],[]]
        for y in range(6):
            for x in range(7): self.board[y].append(0)



class Player:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
