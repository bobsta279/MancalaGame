class Game:
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    playerTurn = 1
    BOARD_SIZE = 14

    def setBoard(self, newBoard):
        self.board = newBoard

    def playerOneTurn(self, chosenSlot):
        if playerTurn != 1:
            print("Not player 1\'s turn")
            return
        if(advanceSlot(chosenSlot) is False):
            print("player 1 turn ended")
            playerTurn = 2
        else:
            print("player 1 earned another turn")

    def playerOneTurn(self, chosenSlot):
        if playerTurn != 2:
            print("Not player 2\'s turn")
            return
        if(advanceSlot(chosenSlot) is False):
            print("player 2 turn ended")
            playerTurn = 1
        else:
            print("player 2 earned another turn")

    def advanceSlot(self, slotNum):
        stonesInHand = board[slotNum]
        board[slotNum] = 0
        counter = 1
        while stonesInHand > 0:
            if playerTurn = 1:
                if (slotNum + counter) % BOARD_SIZE != 13:
                    stonesInHand -= 1
                    board[(slotNum + counter) % BOARD_SIZE] += 1
            elif playerTurn = 2:
                if (slotNum + counter) % BOARD_SIZE != 6:
                    stonesInHand -= 1
                    board[(slotNum + counter) % BOARD_SIZE] += 1

            counter += 1

    def getBoard(self):
        return board

    