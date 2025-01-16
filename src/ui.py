from src.board import ConnectFourBoard
from src.exceptions import BoardException, GameOver
from src.game import ConnectFourGame
from colorama import Fore, Style

class UI:
    def __init__(self):
        self.__playerBoard = ConnectFourBoard()

        self.__game = ConnectFourGame(self.__playerBoard)

    def printBoards(self):
        print(Fore.GREEN)
        print("Your board:")
        print(self.__playerBoard)
        print(Style.RESET_ALL)

        print(Fore.RED)
        print("Computer's board:")
        print(self.__playerBoard)
        print(Style.RESET_ALL)

    def startGame(self):
        print("Welcome to Connect Four!")
        self.printBoards()

        playerTurn = True
        while True:
            if playerTurn:
                try:
                    column = int(input("Choose a column (0-6): "))
                    row, column = self.__game.dropPlayerPiece(column)
                    self.printBoards()
                    if self.__playerBoard.checkWin(row, column, 'X'):
                        print("You win!")
                        self.printBoards()
                        break
                    playerTurn = False
                except GameOver:
                    print("Game Over!")
                    self.printBoards()
                    break
                except BoardException as e:
                    print(e)
            else:
                row, column = self.__game.dropComputerPiece()
                print(f"Computer chose column {column}")
                self.printBoards()
                if self.__playerBoard.checkWin(row, column, 'O'):
                    print("Computer wins!")
                    self.printBoards()
                    break
                playerTurn = True
