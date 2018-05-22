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

    def play(self, space):
        print(space)
        for i, item in reversed(list(enumerate(self.board))):
            print(i, item)
            if item[space] == 0:
                self.board[i][space] = self.turn
                return
            continue
        return

    def check(self, check_hor=False, check_ver=True):
        # set the hor and ver values in a more user friendly manner
        hor, ver = 0, 0
        if check_hor: hor = 4
        if check_ver: ver = 4

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
                            if self.board[y+a][x+b] == self.turn: continue # check if xy point + ab is the players value
                            else: raise IndexError # if not then raise IndexError, effectivly skipping to next value
                        return True# else return True
                    except IndexError: continue # if run to end of table, move to next value
        return False # if all values are checked, and not returned True, return False





class Player:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
