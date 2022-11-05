class mGame:
    def __init__(self):
        #creates game board
        #player 1s side is 0-5, with their mancala at 6
        #player 2s side is 7-12 with their mancala at 13
        self.board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]

    def play(self):
        while True:
            print(self.string())
            if self.p1move() == 1:
                break
            print(self.string())
            if self.p2move() == 1:
                break
        print("Game over!")
        print("Points Player 1: ", self.board[6])
        print("Points Player 2: ", self.board[13])
        

    def string(self):
        return str(self.board[13]) +"  "+ str(list(reversed(self.board))[1:7]) + "\n   " + str(self.board[0:6]) +"  "+ str(self.board[6])

    def p1move(self):
        #reads input from player and rejects it if necessary
        n = int(input("Player 1: "))
        if n > 5 or n < 0 or self.board[n] == 0:
            print("Invalid move")
            self.p1move()
            return
        #empties chosen space and places pieces forward
        #skips player 2s mancala
        f = self.board[n]
        self.board[n] = 0
        p = n+1
        while f > 0:
            if p != 13:
                self.board[p] += 1
                p += 1
                f -= 1
            else:
                p = 0
        #checks board for game end condition
        t = True
        for p in self.board[0:6]:
            if p != 0:
                t = False
                break
        #gives points to other player and ends game
        if t == True:
            for p in self.board[7:13]:
                self.board[13] += p
            return 1


    def p2move(self):
        #reads input from player and rejects it if necessary
        n = int(input("Player 2: "))
        if n > 5 or n < 0 or self.board[n+7] == 0:
            print("Invalid move")
            self.p2move()
            return
        #empties chosen space and places pieces forward
        #skips player 1s mancala, and skips to beginning when reaches own mancala
        f = self.board[n+7]
        self.board[n+7] = 0
        p = n+8
        while f > 0:
            if p < 14 and p != 6:
                self.board[p] += 1
                p += 1
                f -= 1
            elif p == 14:
                p = 0
            elif p == 6:
                p = 7
        #checks board for game end condition
        t = True

        for p in self.board[7:13]:
            if p != 0:
                t = False
                break
        #gives points to other player and ends game
        if t == True:
            for p in self.board[0:6]:
                self.board[6] += p
            return 1


