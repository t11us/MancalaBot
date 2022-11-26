from mGame import mGame

class miniMax:

    def __init__(self, board):
        self.board = board
        self.bs = [0]*4
    
    def move(self):
        score = -float("inf")
        move = 0
        b = mGame()
        print(type(b))
        state = self.board.boardState()
        print("startstate, " ,state)
        for i in range(0,6):
            b.setState(state)
            print("b1, ", b)
            s = self.minimax(1, 1, b)
            if s > score:
                score = s
                move = i
        return move

    def minimax(self, turn, left, b):
        b = b
        print("b, " ,b)
        state = b.boardState()
        print("mini: ", self, turn, left, state, self.bs[left])
        scores = []
        if left > 0:
            for i in range(0,6):
                
                b.setState(state)
                
                if turn == 0 and b.boardState()[i] != 0:
                    b.p1move(i)
                elif b.boardState()[i+7] != 0:
                    b.p2move(i)
                else: 
                    pass
                scores.append(self.minimax(1-turn, left-1, b))
                b.setState(state)
            if turn == 0: 
                return max(scores)
            else:
                return min(scores)
        else:
            print("heru, ", state)
            return self.heuristic(state)


    def heuristic(self, state):
        p = 0
        for n in range(0,6):
            p += state[n]
        p += 2 * state[6]
        for n in range(7,13):
            p -= state[n]
        p -= 2* state[13]
