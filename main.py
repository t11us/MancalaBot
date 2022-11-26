from mGame import mGame
from minMax import miniMax

def main():
    #creates game
    m = mGame()
    #alternates turns until end condition reached
    while True:
        if m.turn == 1:
            print(m.string())
            move = input("Player 1: ")
            if m.p1move(move):
                break
        if m.turn == 2:
            #failed implementation of minimax
            #b = mGame()
            #b.setState(m.boardState())
            #print(m.string())
            #mini = miniMax(b)
            #move = mini.move()
            #print("Player 2: ", move)
            #if m.p2move(move):
                #break
            print(m.string())
            move = input("Player 2: ")
            if m.p2move(move):
                break
    #prints points at end of game
    print("Game over!")
    print("Points Player 1: ", m.board[6])
    print("Points Player 2: ", m.board[13])
    if m.board[6] > m.board[13]:
        print("Player 1 wins!")
    if m.board[6] == m.board[13]:
        print("It's a tie!")
    else:
        print("Player 2 wins!")
        

if __name__ == "__main__":
    main()

def play():
    board 
        