import unittest

from pyrpn.rpn import eval_rpn

class TestRPN(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(3, eval_rpn('1  2    +'))
        self.assertEqual(4, eval_rpn('2 2 +'))
        self.assertEqual(1, eval_rpn('-4 5 +'))

    def test_soustraction(self):
        self.assertEqual(1, eval_rpn('3 2 -'))
        self.assertEqual(4, eval_rpn('3 2 1 - +'))

    def test_acceptance(self):
        self.assertEqual(2, eval_rpn('4 2 5 * + 1 3 2 * + /'))

    def test_acceptance2(self):
        self.assertEqual(14, eval_rpn('5 1 2 + 4 * 3 - +'))
