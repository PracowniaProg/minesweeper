from source.board.board_generator import pos_correct
import unittest

class TestPos_correct(unittest.TestCase):

    def test_first_less(self):
        self.assertEqual(pos_correct(6, 6, -1, 3), False)

    def test_second_less(self):
        self.assertEqual(pos_correct(7, 9, -5, -9), False)

    def test_first_more(self):
        self.assertEqual(pos_correct(7, 21, 9, 15), False)

    def test_second_more(self):
        self.assertEqual(pos_correct(37, 37, 9, 40), False)

    def test_both_correct(self):
        self.assertEqual(pos_correct(10, 10, 6, 7), True)

if __name__ == '__main__':
    unittest.main()