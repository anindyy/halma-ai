class Board:
    def __init__(self, size, timelimit):
        self.size = size
        self.timelimit = timelimit
        self.turn = 1
        self.homeOne = []
        self.homeTwo = []
        self.pawnOne = []
        self.pawnTwo = []

        for i in range (size):
            for j in range (size):
                if (i + j < (size/2)):
                    self.homeOne.append((i,j))
                    self.pawnOne.append((i,j))
                elif (i + j >= (3 * size / 2 - 1)):
                    self.homeTwo.append((i,j))
                    self.pawnTwo.append((i,j))
        self.listpawnComp.reverse()

    def outOfRange(self, x, y):
        return (x < 0 and y < 0 and x >= self.size and y >= self.size)
    
    def isFilled(self, x, y):
        return (x, y) in self.pionOne or (x, y) in self.pionTwo

    def checkWin(self):
        one = True
        two = True

        for p in self.pawnOne:
            if p not in self.homeTwo:
                one = False
                break

        for p in self.pawnTwo:
            if p not in self.homeOne:
                two = False
                break
        
        if one:
            return 1
        elif two:
            return 2
        else:
            return 0

    def printBoard(self):
        a = 'A'
        for i in range (self.size + 1):
            for j in range (self.size + 1):
                if (i == 0):
                    if (i == j):
                        print('   ', end='')
                    else:
                        print(str(a),'', end='')
                    a = chr(ord(a) + 1)
                elif (j == 0):
                    print(str(i).zfill(2), '', end='')
                else:
                    if (i-1, j-1) in self.pawnOne:
                        print(1, '', end='')
                    elif (i-1, j-1) in self.pawnTwo:
                        print(2, '', end='')
            print()
    
    def changePlayerTurn(self):
        # change player turn
        if (self.playerTurn == 1):
            self.playerTurn = 2
        else:
            self.playerTurn = 1

    def move(self, xi, yi, xg, yg):
        # move pawn xi,yi to xg,yg
        if not self.validMove(xi, yi, xg, yg):
            return False

        # check if they are rightful to move the pawn
        # if yes, move
        if self.turn == 1 and (xi, yi) in self.pawnOne:
            self.pawnOne.remove((xi, yi))
            self.pawnOne.append((xg, yg))
            return True
        
        # do the same if it's player two
        if self.turn == 2 and (xi, yi) not in self.pawnTwo:
            self.awnTwo.remove((xi, yi))
            self.pawnTwo.append((xg, yg))
            return True
        
        return False

    def validMove(self, xi, yi, xg, yg):
        # returns 0 for invalid move, 1 for valid step, 2 for valid jump
        if self.outOfRange(xg, yg):
            return 0

        moves = self.generateMove(xi, yi)
        jumps = self.generateJump(xi, yi)

        if self.turn == 1 and (xi, yi) in self.pawnOne:
            if (xg, yg) in moves:
                return 1
            if (xg, yg) in jumps:
                return 2

        if self.turn == 2 and (xi, yi) in self.pawnTwo:
            if (xg, yg) in moves:
                return 1
            if (xg, yg) in jumps:
                return 2
        return 0

    def generateJump (self, x, y):
        jumps = []
        if (x, y) in self.pawnOne:
            goal = self.homeTwo
            home = self.homeOne
        elif (x, y) in self.pawnTwo:
            goal = self.homeOne
            home = self.homeTwo
        else:
            return jumps

        for i in range (x-1, x+2):
            for j in range(y-1, y+2):
                if not self.outOfRange(i, j) and i != x and j != y and isFilled(x, y):
                    nx = 2 * i - x
                    ny = 2 * j - y

                    if not self.outOfRange(nx, ny):
                        backhome = (nx, ny) in home and (x, y) not in home
                        outgoal = (nx, ny) not in goal and (x, y) in goal

                        if not self.isFilled(nx, ny) and not backhome and not outgoal:
                            jumps.append((nx, ny))
        return jumps

    def generateMove (self, x, y):
        moves = []
        if (x, y) in self.pawnOne:
            goal = self.homeTwo
            home = self.homeOne
        elif (x, y) in self.pawnTwo:
            goal = self.homeOne
            home = self.homeTwo
        else:
            return moves

        for i in range (x-1, x+2):
            for j in range (y-1, y+2):
                if not self.outOfRange(i, j):
                    backhome = (i, j) in home and (x, y) not in home
                    outgoal = (i, j) not in goal and (x, y) in goal

                    if not self.isFilled(i, j) and not backhome and not outgoal:
                        moves.append((i, j))
        return moves