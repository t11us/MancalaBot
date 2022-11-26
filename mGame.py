class mGame:

    #creates game board
    #player 1s side is 0-5, with their mancala at 6
    #player 2s side is 7-12 with their mancala at 13
    #turn tracks whose turn it is
    def __init__(self):
        self.board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
        self.turn = 1
        
    #returns string of self for printing in terminal
    def string(self):
        s = "  "
        z = "  "
        q = " " * (3-len(str(self.board[13])))
        for i in range (0,6):
            s = s + "  " + str(i)
            z = z + "  " + str(5-i)
        return z + "\n" + str(self.board[13]) + q + str(list(reversed(self.board))[1:7]) + "\n   " + str(self.board[0:6]) +"  "+ str(self.board[6]) + "\n" + s

    #returns board state
    def boardState(self):
        return self.board
    
    #takes 14-long list and sets it as game state
    def setState(self, state):
        self.board = state

    #sets int as turn state
    def setTurn(self, turn):
        self.turn = turn

    #checks for end condition and ends game if found
    def isEnd(self):
        t = True
        d = True
        #if either side has no pieces in it, the end condition is True
        for h in self.board[0:6]:
            if h != 0:
                t = False
                break
        for h in self.board[7:13]:
            if h != 0:
                d = False
                break
        #gives points to other player and ends game if end condition is True
        if t == True or d == True:
            for h in self.board[7:13]:
                self.board[13] += h
            for h in self.board[0:6]:
                self.board[6] += h
            return 1
    
    #checks whether pieces have been captured, and moves them to the appropriate mancala if so
    def isCapture(self, p):
        #check whether stones are captured
        if self.board[13-p] != 0 and self.board[p-1] == 1:
            #add stones to appropriate mancala
            if p < 7:
                self.board[6] += self.board[13-p]+1
                print("Player 1 has captured pieces")
            else: 
                self.board[13] += self.board[13-p]+1
                print("Player 2 has captured pieces")
            #remove captured stones from board
            self.board[13-p] = 0
            self.board[p-1] = 0

    
                
    #move for player 1. repeats turn, gives turn to p2 or ends game at end
    def p1move(self, n):
        self.repeat = False
        #reads new input from player if invalid
        while int(n) > 5 or int(n) < 0 or self.board[n] == 0:
            n = input("Invalid move\nPlayer 1: ")
        #empties chosen space and places pieces forward
        #skips player 2s mancala and returns to 0
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
        #check for capturing stones
        if p < 7 and p > 0:
            self.isCapture(p)
        #checks board for game end condition
        if self.isEnd():
            return 1
        #checks if player should get another turn, else gives turn to p2
        if p != 7:
            self.turn = 2

    #move for player 2, the ai. repeats turn, gives turn to p2 or ends game at end
    def p2move(self,n):
        #empties chosen space and places pieces forward
        #skips player 1s mancala, and skips to beginning when reaches own mancal
        f = self.board[n+7]
        self.board[n+7] = 0
        p = n+8
        while f > 0:
            if p < 13 and p != 6:
                self.board[p] += 1
                p += 1
                f -= 1
            elif p == 13:
                self.board[p] += 1
                p = 0
                f -= 1
            elif p == 6:
                p = 7
        #check for capturing stones
        if p > 7:
            self.isCapture(p)
        #checks board for game end condition
        if self.isEnd():
            return 1
        #checks if player should get another turn, else gives turn to p1
        print(p)
        if p != 0:
            self.turn = 1

