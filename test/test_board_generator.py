from source.board.board_generator import generate_board
from source.settings import VALUES_OF_BOARD_FIELDS
import unittest

class TestBoard_generator(unittest.TestCase):

    def test_correct_size(self):
        board = generate_board(10, 12, 6)
        self.assertEqual(len(board), 10)
        self.assertEqual(len(board[0]), 12)

    def test_normal_case(self):
        board = generate_board(8, 8, 10)
        mines = 0
        for i in range(8):
            for j in range(8):
                if board[i][j].value == VALUES_OF_BOARD_FIELDS["BOMB"]:
                    mines = mines + 1

        self.assertEqual(mines, 10)

    def test_no_mines(self):
        board = generate_board(5, 5, 0)
        mines = 0
        for i in range(5):
            for j in range(5):
                if board[i][j].value == VALUES_OF_BOARD_FIELDS["BOMB"]:
                    mines = mines + 1

        self.assertEqual(mines, 0)

    def test_no_size_but_some_mines(self):
        with self.assertRaises(IndexError):
            board = generate_board(0, 0, 5)

if __name__ == '__main__':
    unittest.main()