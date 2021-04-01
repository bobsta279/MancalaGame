from Game import Game

def main():
    board = []
    # for i in range(14):
        # print()
        # numPebbles = int(input("What is in spot " + str(i) + " on the board?\n"))
        # board.append(numPebbles)
    board = [3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 0]
        
    game = Game(board)
    game.printBoard()
    
    while not game.isGameOver():
        while game.playerTurn == 1:
            userInput = input("What spot does player one choose?\n")
            if userInput == '':
                print("Boi")
                continue
            chosenSlot = int(userInput)
            if(chosenSlot < 0 or chosenSlot > 6):
                print("Invalid slot chosen. Retry")
            game.playerOneTurn(chosenSlot)
            game.printBoard()
        
        if game.isGameOver():
            break
        
        while game.playerTurn == 2:
            userInput = input("What spot does player two choose?\n")
            if userInput == '':
                print("Boi")
                continue
            chosenSlot = int(userInput)
            if(chosenSlot < 7 or chosenSlot > 12):
                print("Invalid slot chosen. Retry")
            game.playerTwoTurn(chosenSlot)
            game.printBoard()
            
    finalBoard = game.getBoard()
    if finalBoard[:7] > finalBoard[7:]:
        print("Player 1 WINS")
        print("Player 2 LOSES")
    elif finalBoard[:7] < finalBoard[7:]:
        print("Players 2 WINS")
        print("Player 1 LOSES")
    else:
        print("It\'s a Tie")  
        
    print("Thanks for playing!")
    
if __name__ == "__main__":
    main()