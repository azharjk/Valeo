import unittest

from project.valeo import valeo_debug_string, valeo_eval

class AppTest(unittest.TestCase):
    def test_empty_input(self):
        result = valeo_debug_string('')
        self.assertEqual(result, None)

    @unittest.skip('Not implemented yet')
    def test_whitespaces_input(self):
        result1 = valeo_eval('1 + 1')
        self.assertEqual(result1, 2)

        result2 = valeo_eval('10 ')
        self.assertEqual(result2, 42)

