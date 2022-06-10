import unittest

from project.valeo import valeo_debug_string, valeo_eval

class AppTest(unittest.TestCase):
    def test_empty_input(self):
        result = valeo_debug_string('')
        self.assertEqual(result, None)

    def test_single_number_in_paren(self):
        result = valeo_eval('(10)')
        self.assertEqual(result, 10)

    def test_only_paren(self):
        result = valeo_eval('()')
        self.assertEqual(result, None)

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

    @unittest.skip('Not implemented yet')
    def test_whitespaces_input(self):
        result1 = valeo_eval('1 + 1')
        self.assertEqual(result1, 2)

        result2 = valeo_eval('10 ')
        self.assertEqual(result2, 42)

