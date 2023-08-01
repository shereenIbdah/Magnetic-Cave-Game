import copy
import time as t
class square:
    def __init__(self):
        self.value = 'E'
        self.__validity = False

    # define setter
    def setValidity(self, validity):
        self.__validity = validity

    # define getter
    def getValidity(self):
        return self.__validity

board = [[square() for i in range(8)] for j in range(8)]

# define method to print the board
def printBoard(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j].value, end=" ")

        print()

# define method to check if square is empty or not  x,y inputs from player
def isEmptySqaure(board, x, y):
    if board[x][y].value == 'E':
        return True
    else:
        return False

def initialState(board):
    # make the validito for column 0 and 7 as true
    for i in range(8):
        board[i][0].setValidity(True)
        board[i][7].setValidity(True)

# define method to check if the move is valid or not
def isValidMove(board, x, y):
    if board[x][y].getValidity() == True:
        return True
    else:
        return False

# main method
def playGame():
    print("Welcome to the game of Magnetic Cave.")
    print("Here is the initial board.")
    printBoard(board)
    currentPlayer = "■"
    initialState(board)
    print("Here is the initial board.")
    menu()
    mode = int(input("Enter the mode you want to play: "))
    # if mode value other than 1,2,3 then ask again
    while mode != 1 and mode != 2 and mode != 3:
        print("Invalid mode")
        mode = int(input("Enter the mode you want to play: "))
    while True:
        if mode == 1:
            print("There are two players in this game. ■ and □")
            print("It is " + currentPlayer + "'s turn.")
            print("Enter your starting position of the Magnetic Cave !! ")
            try:
                row = int(input("Enter the row number: "))
            except ValueError:
                print("Invalid row number")
                row = int(input("Enter the row number: "))
            if row < 0 or row > 7:
                print("Invalid row number")
                continue
            column = int(input("Enter the column number: "))
            if column < 0 or column > 7:
                print("Invalid column number")
                continue
            if isEmptySqaure(board, row, column) and isValidMove(board, row, column):
                print("Valid move")
                board[row][column].value = currentPlayer
                board[row][column].setValidity(False)
                updateValidation(board, row, column)
                printBoard(board)
                print("The nearness to victory for " + currentPlayer + " is: ")
                print(nearness_to_victory(board, currentPlayer))
                if checkWinner(board, currentPlayer):
                    print("Player " + currentPlayer + " wins")
                    print("Game Ended")
                    break
                # else if the board is full and no one wins then it is a draw
                else:
                    flag = True
                    for i in range(8):
                        for j in range(8):
                            if board[i][j].value == "E":
                                flag = False
                    if flag:
                        print("you both are equally good no one wins")
                        break
            else:
                print("Invalid move , try again please")
                continue
            currentPlayer = togglePlayer(currentPlayer)

        elif mode == 2:
            print("In This mode You ■ and the computer is □  ")
            print("It is " + currentPlayer + "'s turn.")
            print("Enter your position of the Magnetic Cave !! ")
            row = int(input("Enter the row number: "))
            if row < 0 or row > 7:
                print("Invalid row number")
                continue
            column = int(input("Enter the column number: "))
            if column < 0 or column > 7:
                print("Invalid column number")
                continue
            if isEmptySqaure(board, row, column) and isValidMove(board, row, column):
                print("Valid move")
                board[row][column].value = currentPlayer
                board[row][column].setValidity(False)
                updateValidation(board, row, column)
                printBoard(board)
                if checkWinner(board, currentPlayer):
                    print("Player " + currentPlayer + " wins")
                # else if the board is full and no one wins then it is a draw
                else:
                    flag = True
                    for i in range(8):
                        for j in range(8):
                            if board[i][j].value == "E":
                                flag = False
                    if flag:
                        print("you both are equally good no one wins")
                        break
            else:
                print("Invalid move , try again please")
                continue
            print("It is " + togglePlayer(currentPlayer) + "'s turn.")
            boardcopy = copy.deepcopy(board)
            currentPlayer2 = currentPlayer
            start = t.time()
            bestscore, bestmove = minimax(boardcopy, 2, False, float('-inf'), float('inf'), currentPlayer2, mode)
            end = t.time()
            print("The time for the minimax algorithm is: ", end - start)
            currentPlayer = togglePlayer(currentPlayer)
            board[bestmove[0]][bestmove[1]].value = currentPlayer
            board[bestmove[0]][bestmove[1]].setValidity(False)
            updateValidation(board, bestmove[0], bestmove[1])
            printBoard(board)
            # check if the current player wins
            if checkWinner(board, currentPlayer):
                print("Player " + currentPlayer + " wins")
                print("Game Ended")
                break
            else:
                flag = True
                for i in range(8):
                    for j in range(8):
                        if board[i][j].value == "E":
                            flag = False
                if flag:
                    print("you both are equally good no one wins")
                    break
            #print(bestscore, bestmove)
            currentPlayer = togglePlayer(currentPlayer)
        elif mode == 3:
            print("The first player is AI, and the second player is Human")
            print("It is " + currentPlayer + "'s turn.")
            boardcopy = copy.deepcopy(board)
            currentPlayer2 = currentPlayer
            start = t.time()
            bestscore, bestmove = minimax(boardcopy,2, True, float('-inf'), float('inf'), currentPlayer2, mode)
            end = t.time()
            print("The time for the minimax algorithm is: ", end - start)
            board[bestmove[0]][bestmove[1]].value = currentPlayer
            board[bestmove[0]][bestmove[1]].setValidity(False)
            updateValidation(board, bestmove[0], bestmove[1])
            printBoard(board)
            # Check if the AI wins
            if checkWinner(board, currentPlayer):
                print("Player " + currentPlayer + " wins")
                print("Game Ended")
                break
            else:
                flag = True
                for i in range(8):
                    for j in range(8):
                        if board[i][j].value == "E":
                            flag = False
                if flag:
                    print("Both players are equally good. No one wins.")
                    break

            currentPlayer = togglePlayer(currentPlayer)
            print("It is " + currentPlayer + "'s turn.")

            valid_move = False
            while not valid_move:
                print("Enter your position of the Magnetic Cave !! ")
                row = int(input("Enter the row number: "))
                if row < 0 or row > 7:
                    print("Invalid row number")
                    continue
                column = int(input("Enter the column number: "))
                if column < 0 or column > 7:
                    print("Invalid column number")
                    continue

                if isEmptySqaure(board, row, column) and isValidMove(board, row, column):
                    valid_move = True
                else:
                    print("Invalid move Try again.")

            print("Valid move")
            board[row][column].value = currentPlayer
            board[row][column].setValidity(False)
            updateValidation(board, row, column)
            printBoard(board)

            # Check if the human player wins
            if checkWinner(board, currentPlayer):
                print("Player " + currentPlayer + " wins")
                print("Game Ended")
                break
            else:
                flag = True
                for i in range(8):
                    for j in range(8):
                        if board[i][j].value == "E":
                            flag = False
                if flag:
                    print("Both players are equally good. No one wins.")
                    break

            currentPlayer = togglePlayer(currentPlayer)

def menu():
    print("You ca play this game in three modes. ")
    print("1. manual entry for both ■’s moves and □’s moves \n2."
          " manual entry for ■’s moves & automatic moves for □\n3."
          " manual entry for □’s moves & automatic moves for ■")

def togglePlayer(currentPlayer):
    if currentPlayer == "■":
        currentPlayer = "□"
    else:
        currentPlayer = "■"
    return currentPlayer

def checkWinner(board, currentPlayer):
    if checkFiveInColumn(board, currentPlayer) or checkFiveInDiagonal(board, currentPlayer) or checkFiveInRow(
            board, currentPlayer):
        return True
    else:
        return False


# define method to update the validity of the squares
def updateValidation(board, row, column):
    # update the validity of the squares in the same row
    if column == 0:
        board[row][column + 1].setValidity(True)
    elif column == 7:
        board[row][column - 1].setValidity(True)
    else:
        if board[row][column + 1].value != "E":
            board[row][column - 1].setValidity(True)
        elif board[row][column - 1].value != "E":
            board[row][column + 1].setValidity(True)

# defining method to check 5 of current player in a row
def checkFiveInRow(board, currentPlayer):
    for i in range(8):
        for j in range(4):
            if board[i][j].value == currentPlayer and board[i][j + 1].value == currentPlayer and board[i][
                j + 2].value == currentPlayer and board[i][j + 3].value == currentPlayer and board[i][
                j + 4].value == currentPlayer:
                return True
    return False


# defining method to check 5 of current player in a column
def checkFiveInColumn(board, currentPlayer):
    for i in range(4):
        for j in range(8):
            if board[i][j].value == currentPlayer and board[i + 1][j].value == currentPlayer and board[i + 2][
                j].value == currentPlayer and board[i + 3][j].value == currentPlayer and board[i + 4][
                j].value == currentPlayer:
                return True
    return False


# defining method to check 5 of current player in a diagonal
def checkFiveInDiagonal(board, currentPlayer):
    for i in range(4):
        for j in range(4):
            if board[i][j].value == currentPlayer and board[i + 1][j + 1].value == currentPlayer and board[i + 2][
                j + 2].value == currentPlayer and board[i + 3][j + 3].value == currentPlayer and board[i + 4][
                j + 4].value == currentPlayer:
                return True
    return False


def nearness_to_victory(board, currentPlayer):
    max_count = 0
    # Check rows
    for row in board:
        count = 0
        for cell in row:
            if cell.value == currentPlayer:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

    # Check columns
    for col in range(len(board[0])):
        count = 0
        for row in range(len(board)):
            if board[row][col].value == currentPlayer:
                # 0print(board[row][col].value)
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

    # Check diagonals (top left to bottom right)
    for r in range(len(board)):
        count = 0
        for i in range(min(len(board) - r, len(board))):
            if board[r + i][i].value == currentPlayer:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

    for c in range(1, len(board[0])):
        count = 0
        for i in range(min(len(board[0]) - c, len(board))):
            if board[i][c + i].value == currentPlayer:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
    # Check diagonals (top right to bottom left)
    for r in range(len(board)):
        count = 0
        for i in range(min(len(board) - r, len(board))):
            if board[r + i][len(board) - 1 - i].value == currentPlayer:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
    for c in range(1, len(board[0])):
        count = 0
        for i in range(min(len(board[0]) - c, len(board))):
            if board[i][len(board[0]) - 1 - (c + i)].value == currentPlayer:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
    return max_count


# definig minimax algorithm
def minimax(board, depth, isMaximizingPlayer, alpha, beta, currentPlayer, mode):
    board2 = copy.deepcopy(board)
    currentPlayer = togglePlayer(currentPlayer)
    bestMove = None  # Variable to store the best move
    if depth == 0:
        if mode == 2:
            return nearness_to_victory(board, "■"), bestMove
        else:
            return nearness_to_victory(board, "□"), bestMove
    if isMaximizingPlayer:
        bestScore = -1000000
        for i in range(8):
            for j in range(8):
                if board[i][j].value == "E" and board[i][j].getValidity() == True:
                    board[i][j].value = currentPlayer
                    board[i][j].setValidity(False)
                    updateValidation(board, i, j)
                    score, _ = minimax(board, depth - 1, False, alpha, beta, currentPlayer, mode)
                    board = copy.deepcopy(board2)
                    if score > bestScore:
                        bestScore = score
                        bestMove = (i, j)  # Update the best move
                    alpha = max(alpha, bestScore)
        return bestScore, bestMove
    else:
        bestScore = 100000000
        for i in range(8):
            for j in range(8):
                if board[i][j].value == "E" and board[i][j].getValidity() == True:
                    board[i][j].value = currentPlayer
                    board[i][j].setValidity(False)
                    updateValidation(board, i, j)
                    score, _ = minimax(board, depth - 1, True, alpha, beta, currentPlayer, mode)
                    board = copy.deepcopy(board2)
                    if score < bestScore:
                        bestScore = score
                        bestMove = (i, j)  # Update the best move
                    beta = min(beta, bestScore)
        return bestScore, bestMove


try:
    playGame()
except KeyboardInterrupt:
    print("Game terminated by the user")
    exit()
