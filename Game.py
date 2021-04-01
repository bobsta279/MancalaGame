class Game:
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    playerTurn = 1
    BOARD_SIZE = 14

    def __init__(self, board):
        self.board = board
        self.playerTurn = 1
        
    def playerOneTurn(self, chosenSlot):
        if self.playerTurn != 1:
            print("Not player 1\'s turn")
            return
        if(chosenSlot < 0 or chosenSlot > 5 or self.board[chosenSlot] == 0):
            print("Invalid slot chosen. Retry")
            return
        if(self.advanceSlot(chosenSlot) is False):
            print("player 1 turn ended")
            self.playerTurn = 2
        else:
            print("player 1 earned another turn")

    def playerTwoTurn(self, chosenSlot):
        if self.playerTurn != 2:
            print("Not player 2\'s turn")
            return
        if(chosenSlot < 7 or chosenSlot > 12 or self.board[chosenSlot] == 0):
            print("Invalid slot chosen. Retry")
            return
        if(self.advanceSlot(chosenSlot) is False):
            print("player 2 turn ended")
            self.playerTurn = 1
        else:
            print("player 2 earned another turn")

    def advanceSlot(self, slotNum):
        stonesInHand = self.board[slotNum]
        self.board[slotNum] = 0
        counter = 1
        while stonesInHand > 0:
            if self.playerTurn == 1:
                if (slotNum + counter) % self.BOARD_SIZE != 13:
                    stonesInHand -= 1
                    self.board[(slotNum + counter) % self.BOARD_SIZE] += 1
            elif self.playerTurn == 2:
                if (slotNum + counter) % self.BOARD_SIZE != 6:
                    stonesInHand -= 1
                    self.board[(slotNum + counter) % self.BOARD_SIZE] += 1

            counter += 1
        
        lastSlot = (slotNum + counter - 1) % self.BOARD_SIZE
        # If the last stone landed in an empty spot on your side
        if self.board[lastSlot] == 1:
            if lastSlot < 6 and self.playerTurn == 1:
                print("player one stole from player two!")
                slotToStealFrom = lastSlot + (2 * (6 - lastSlot))
                self.board[6] += self.board[lastSlot] + self.board[slotToStealFrom]
                print("They stole " + str(self.board[slotToStealFrom]) + " pebbles")
                self.board[lastSlot] = 0
                self.board[slotToStealFrom] = 0
            if lastSlot > 7 and lastSlot < 13 and self.playerTurn == 2:
                print("player two stole from player one!")
                slotToStealFrom = lastSlot - (2 * (lastSlot - 6))
                self.board[13] += self.board[lastSlot] + self.board[slotToStealFrom]
                print("They stole " + str(self.board[slotToStealFrom]) + " pebbles")
                self.board[lastSlot] = 0
                self.board[slotToStealFrom] = 0
        
            
        # If the last stone landed in the your endzone
        if lastSlot == 6 and self.playerTurn == 1:
            return True
        elif lastSlot == 13 and self.playerTurn == 2:
            return True
        return False

    def getBoard(self):
        return self.board

    def printBoard(self):
        print(self.board)
        
    def isGameOver(self):
        print(sum(self.board[0:6]))
        if sum(self.board[0:6]) == 0 or sum(self.board[7:14]) == 0:
            return True
        return False