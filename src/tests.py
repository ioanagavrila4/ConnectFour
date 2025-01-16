import unittest
from src.exceptions import OutOfBoundsException, ColumnFullException
from src.board import ConnectFourBoard
class TestConnectFourBoard(unittest.TestCase):

    def setUp(self):
        """Set up a new Connect Four board for testing."""
        self.board = ConnectFourBoard()

    def test_drop_piece_success(self):
        """Test dropping a piece in an empty column."""
        row, column = self.board.dropPiece(0, 'X')
        self.assertEqual(row, 5)
        self.assertEqual(column, 0)
        self.assertEqual(self.board._board[row][column], 'X')

    def test_drop_piece_out_of_bounds(self):
        """Test dropping a piece in an invalid column."""
        with self.assertRaises(OutOfBoundsException):
            self.board.dropPiece(-1, 'X')
        with self.assertRaises(OutOfBoundsException):
            self.board.dropPiece(self.board.columns, 'X')

    def test_drop_piece_column_full(self):
        """Test dropping a piece in a full column."""
        for _ in range(self.board.rows):
            self.board.dropPiece(0, 'X')
        with self.assertRaises(ColumnFullException):
            self.board.dropPiece(0, 'X')

    def test_check_win_horizontal(self):
        """Test horizontal win condition."""
        for col in range(4):
            self.board.dropPiece(col, 'X')
        self.assertTrue(self.board.checkWin(5, 3, 'X'))  # Last piece completes horizontal win

    def test_check_win_vertical(self):
        """Test vertical win condition."""
        for _ in range(4):
            self.board.dropPiece(0, 'X')
        self.assertTrue(self.board.checkWin(2, 0, 'X'))  # Last piece completes vertical win

    def test_check_win_diagonal_1(self):
        """Test diagonal (\) win condition."""
        # Create diagonal \
        self.board.dropPiece(0, 'X')
        self.board.dropPiece(1, 'O')
        self.board.dropPiece(1, 'X')
        self.board.dropPiece(2, 'O')
        self.board.dropPiece(2, 'O')
        self.board.dropPiece(2, 'X')
        self.board.dropPiece(3, 'O')
        self.board.dropPiece(3, 'O')
        self.board.dropPiece(3, 'O')
        self.board.dropPiece(3, 'X')
        self.assertFalse(self.board.checkWin(2, 2, 'X'))

    def test_check_win_diagonal_2(self):
        """Test diagonal (/) win condition."""
        # Create diagonal /
        self.board.dropPiece(3, 'X')
        self.board.dropPiece(2, 'O')
        self.board.dropPiece(2, 'X')
        self.board.dropPiece(1, 'O')
        self.board.dropPiece(1, 'O')
        self.board.dropPiece(1, 'X')
        self.board.dropPiece(0, 'O')
        self.board.dropPiece(0, 'O')
        self.board.dropPiece(0, 'O')
        self.board.dropPiece(0, 'X')
        self.assertFalse(self.board.checkWin(2, 1, 'X'))

    def test_no_win(self):
        """Test when there is no win condition."""
        self.board.dropPiece(0, 'X')
        self.board.dropPiece(1, 'X')
        self.board.dropPiece(2, 'X')
        self.assertFalse(self.board.checkWin(5, 2, 'X'))  # Not enough pieces for a win


if __name__ == "__main__":
    unittest.main()
