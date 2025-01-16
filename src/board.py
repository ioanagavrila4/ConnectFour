from texttable import Texttable
from src.exceptions import OutOfBoundsException, BoardException

class ConnectFourBoard:
    def __init__(self, rows=6, columns=7):
        self.__rows = rows
        self.__columns = columns
        self._board = [[' ' for _ in range(self.__columns)] for _ in range(self.__rows)]

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns

    def dropPiece(self, column, piece):
        # Check if the column is valid
        if not (0 <= column < self.columns):
            raise OutOfBoundsException()

        # Check if the column is full
        for row in range(self.rows - 1, -1, -1):
            if self._board[row][column] == ' ':
                self._board[row][column] = piece
                return row, column
        raise ColumnFullException()

    def checkWin(self, row, column, piece):
        # Check horizontal, vertical, and diagonal directions
        return (
                self.checkDirection(row, column, piece, 0, 1) or  # Horizontal
                self.checkDirection(row, column, piece, 1, 0) or  # Vertical
                self.checkDirection(row, column, piece, 1, 1) or  # Diagonal /
                self.checkDirection(row, column, piece, 1, -1)  # Diagonal \
        )

    def checkDirection(self, row, column, piece, delta_row, delta_column):
        count = 0
        # Check in one direction
        r, c = row, column
        while 0 <= r < self.rows and 0 <= c < self.columns and self._board[r][c] == piece:
            count += 1
            r += delta_row
            c += delta_column
        # Check in the opposite direction
        r, c = row - delta_row, column - delta_column
        while 0 <= r < self.rows and 0 <= c < self.columns and self._board[r][c] == piece:
            count += 1
            r -= delta_row
            c -= delta_column
        return count >= 4

    def __str__(self):
        table = Texttable()
        table.header([' '] + [str(i) for i in range(self.columns)])
        for row_index, row in enumerate(self._board):
            table.add_row([str(row_index)] + row)
        return table.draw()


class ColumnFullException(BoardException):
    def __init__(self):
        super().__init__("This column is already full!")
