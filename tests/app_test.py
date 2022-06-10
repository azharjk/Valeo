import unittest

from project.valeo import valeo_debug_string, valeo_eval

class AppTest(unittest.TestCase):
    def test_empty_input(self):
        with self.assertRaises(SystemExit) as cm:
            valeo_debug_string('')

        self.assertEqual(cm.exception.code, 1)

    def test_single_number_in_paren(self):
        result = valeo_eval('(10)')
        self.assertEqual(result, 10)

    def test_only_paren(self):
        with self.assertRaises(SystemExit) as cm:
            valeo_eval('()')

        self.assertEqual(cm.exception.code, 1)

    def test_paren_follow_by_expr(self):
        result = valeo_eval('10+(1)')
        self.assertEqual(result, 11)

    def test_basic_expression(self):
        r1 = valeo_eval('100+50')
        self.assertEqual(r1, 150)

        r2 = valeo_eval('65+89*2')
        self.assertEqual(r2, 243)

        r3 = valeo_eval('800/400*72-2')
        self.assertEqual(r3, 142)

        r4 = valeo_eval('(8+8)*25')
        self.assertEqual(r4, 400)

        r5 = valeo_eval('120 * (18) - 45 * (120) + 120 * (32)')
        self.assertEqual(r5, 600)

    def test_whitespaces_input(self):
        r1 = valeo_eval(' 1')
        self.assertEqual(r1, 1)

        r2 = valeo_eval('             67')
        self.assertEqual(r2, 67)

        r3 = valeo_eval('10 ')
        self.assertEqual(r3, 10)

        r4 = valeo_eval('89                ')
        self.assertEqual(r4, 89)

        with self.assertRaises(SystemExit) as cm:
            valeo_eval(' ')

        self.assertEqual(cm.exception.code, 1)

    def test_basic_expression_with_whitespaces(self):
        r1 = valeo_eval('    1    +   1   ')
        self.assertEqual(r1, 2)

        r2 = valeo_eval(' 12  * 2  + 3')
        self.assertEqual(r2, 27)

        r3 = valeo_eval('2 * 2')
        self.assertEqual(r3, 4)

        r4 = valeo_eval('5 + 2 * 2  ')
        self.assertEqual(r4, 9)

        r5 = valeo_eval('(  1 + 2  ) * 2')
        self.assertEqual(r5, 6)

    def test_nested_parenthesis(self):
        result = valeo_eval('(1 + 1- (2*7) + 1) / 2')
        self.assertEqual(result, -5.5)
