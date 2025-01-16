from random import randint
from src.exceptions import BoardException

class ConnectFourGame:
    def __init__(self, board):
        self.__board = board

    def dropPlayerPiece(self, column):
        try:
            row, column = self.__board.dropPiece(column, 'X')
            return row, column
        except BoardException as e:
            print(e)
            return None

    def dropComputerPiece(self):
        blocking_column = self.findBlockingMove()
        if blocking_column is not None:
            try:
                row, column = self.__board.dropPiece(blocking_column, 'O')
                return row, blocking_column
            except BoardException:
                pass

        # pick a random column
        while True:
            column = randint(0, self.__board.columns - 1)
            try:
                row, column = self.__board.dropPiece(column, 'O')
                return row, column
            except BoardException:
                continue  # Retry until a valid column is found

    def simulateDropPiece(self, column, board, piece):
        """Simulate dropping a piece in a column and return a temporary board with the move."""
        if column < 0 or column >= board.columns:
            raise BoardException("Invalid column")

        temp_board = [row[:] for row in board._board]  # Deep copy of the board state
        for row in range(board.rows - 1, -1, -1):
            if temp_board[row][column] == ' ':
                temp_board[row][column] = piece
                return temp_board, row
        raise BoardException("Column is full")

    def findBlockingMove(self):
        """Find a column where the player might win next turn and block it."""
        for col in range(self.__board.columns):
            try:
                temp_board, row = self.simulateDropPiece(col, self.__board, 'X')
                if self.checkWinOnTempBoard(temp_board, row, col, 'X'):
                    return col
            except BoardException:
                continue
        return None

    def checkWinOnTempBoard(self, temp_board, row, column, piece):
        """Check for a win condition on a temporary board."""
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # Horizontal, Vertical, Diagonal /, Diagonal \
        for delta_row, delta_col in directions:
            count = self.__countPieces(temp_board, row, column, piece, delta_row, delta_col)
            count += self.__countPieces(temp_board, row, column, piece, -delta_row, -delta_col) - 1
            if count >= 4:
                return True
        return False

    def __countPieces(self, board, row, col, piece, delta_row, delta_col):
        """Count consecutive pieces in a specific direction."""
        count = 0
        while 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == piece:
            count += 1
            row += delta_row
            col += delta_col
        return count
