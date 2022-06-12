import unittest

from project.valeo import valeo_eval

class ErrorTest(unittest.TestCase):
    def test_unrecognized_char(self):
        with self.assertRaises(SystemExit) as cm:
            valeo_eval(' c ')

        self.assertEqual(cm.exception.code, 1)

    def test_incorrect_expression(self):
        with self.assertRaises(SystemExit) as cm:
            valeo_eval('1+')

        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm:
            valeo_eval(' + - ')

        self.assertEqual(cm.exception.code, 1)

    def test_unclosed_parenthesis(self):
        with self.assertRaises(SystemExit) as cm:
            valeo_eval('(10')

        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm:
            valeo_eval('12 + 2 * (8 + 2')

        self.assertEqual(cm.exception.code, 1)

    def test_nested_unclosed_parethesis(self):
        with self.assertRaises(SystemExit) as cm:
            valeo_eval('(8 + (1 + 1)')

        self.assertEqual(cm.exception.code, 1)

    def test_lparen_recursion(self):
        with self.assertRaises(SystemExit) as cm:
            valeo_eval('(')

        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm:
            valeo_eval('1+(')

        self.assertEqual(cm.exception.code, 1)
