from source.board.board_generator import generate_board
from source.gui.revealing_fields import RevealFields
import unittest

class TestRevealing_fields(unittest.TestCase, RevealFields):

    def test_revealing_flagged(self):
        board = generate_board(10, 10, 10)
        board[5][5].flagged = True

        rev = RevealFields(board, 5, 5)
        rev._reveal_neighbours(5, 5)

        self.assertEqual(board[5][5].flagged, True)
        self.assertEqual(board[5][5].revealed, False)

    def test_revealing_not_flagged(self):
        board = generate_board(10, 10, 10)

        rev = RevealFields(board, 5, 5)
        rev._reveal_neighbours(5, 5)

        self.assertEqual(board[5][5].flagged, False)
        self.assertEqual(board[5][5].revealed, False)

    def test_pos_first_less(self):
        board = generate_board(6, 6, 10)
        rev = RevealFields(board, 6, 6)
        self.assertEqual(rev._is_pos_correct(-1, 3), False)

    def test__pos_second_less(self):
        board = generate_board(7, 9, 10)
        rev = RevealFields(board, 7, 9)
        self.assertEqual(rev._is_pos_correct(-5, -9), False)

    def test_pos_first_more(self):
        board = generate_board(7, 21, 10)
        rev = RevealFields(board, 7, 21)
        self.assertEqual(rev._is_pos_correct(9, 15), False)

    def test_pos_second_more(self):
        board = generate_board(37, 37, 10)
        rev = RevealFields(board, 37, 37)
        self.assertEqual(rev._is_pos_correct(9, 40), False)

    def test_pos_both_correct(self):
        board = generate_board(10, 10, 10)
        rev = RevealFields(board, 10, 10)
        self.assertEqual(rev._is_pos_correct(6, 7), True)

if __name__ == '__main__':
    unittest.main()