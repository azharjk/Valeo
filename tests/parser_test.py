import unittest

from project.parser import AddNode, AstNode, DivNode, MultNode, NumberNode, Parser, SubNode
from project.internal_token import Token, TokenType

class ParserTest(unittest.TestCase):
    def test_instantiate_object(self):
        parser = Parser([])
        self.assertTrue(parser)

    def test_eof_method(self):
        parser = Parser([
            Token(TokenType.PLUS, 0, 1),
            Token(TokenType.MINUS, 0, 2),
            Token(TokenType.ASTERISK, 0, 3),
        ])

        self.assertFalse(parser._eof())
        parser.index = 2
        self.assertTrue(parser._eof())

    def test_peek_method(self):
        parser = Parser([
            Token(TokenType.PLUS, 0, 1),
            Token(TokenType.MINUS, 0, 2),
            Token(TokenType.ASTERISK, 0, 3),
        ])

        self.assertEqual(parser._peek(), Token(TokenType.PLUS, 0, 1))
        parser.index = 1
        self.assertEqual(parser._peek(), Token(TokenType.MINUS, 0, 2))

    def test_consume_method(self):
        parser = Parser([
            Token(TokenType.PLUS, 0, 1),
            Token(TokenType.MINUS, 0, 2),
            Token(TokenType.ASTERISK, 0, 3),
        ])

        self.assertEqual(parser._consume(), Token(TokenType.PLUS, 0, 1))
        self.assertEqual(parser.index, 1)

        parser.index = 2
        self.assertEqual(parser._consume(), Token(TokenType.ASTERISK, 0, 3))
        self.assertEqual(parser.index, 2)

    def test_parse_number_method(self):
        parser = Parser([
            Token(TokenType.NUMBER, 10, 1)
        ])

        self.assertEqual(parser.parse_number()._debug_string(), NumberNode(10)._debug_string())

    def test_parse_number_method_fail(self):
        parser = Parser([
            Token(TokenType.MINUS, 0, 1)
        ])

        self.assertRaises(AssertionError, parser.parse_number)

    def test_parse_paren_method(self):
        parser = Parser([
            Token(TokenType.LPAREN, 0, 1),
            Token(TokenType.NUMBER, 78, 2),
            Token(TokenType.RPAREN, 0, 3)
        ])

        self.assertEqual(parser.parse_paren()._debug_string(), NumberNode(78)._debug_string())

    def test_parse_paren_method_fail(self):
        parser = Parser([
            Token(TokenType.NUMBER, 78, 2),
        ])

        self.assertRaises(AssertionError, parser.parse_paren)

    def test_parse_paren_method_unclosed_paren(self):
        parser = Parser([
            Token(TokenType.LPAREN, 0, 1),
            Token(TokenType.NUMBER, 1, 2),
        ])

        self.assertRaises(AssertionError, parser.parse_paren)

    def test_parse_primary_method_number_case(self):
        parser = Parser([
            Token(TokenType.NUMBER, 55, 1)
        ])

        self.assertEqual(parser.parse_primary()._debug_string(), NumberNode(55)._debug_string())

    def test_parse_primary_method_paren_case(self):
        parser = Parser([
            Token(TokenType.LPAREN, 0, 1),
            Token(TokenType.NUMBER, 67, 1),
            Token(TokenType.RPAREN, 0, 1)
        ])

        self.assertEqual(parser.parse_primary()._debug_string(), NumberNode(67)._debug_string())

    def test_parse_primary_method_unhandled_token_case(self):
        parser = Parser([
            Token(TokenType.ASTERISK, 0, 1)
        ])

        self.assertEqual(parser.parse_primary()._debug_string(), AstNode()._debug_string())

    def test_parse_term_method_mult(self):
        parser = Parser([
            Token(TokenType.NUMBER, 5, 1),
            Token(TokenType.ASTERISK, 0, 2),
            Token(TokenType.NUMBER, 7, 1),
        ])

        self.assertEqual(parser.parse_term()._debug_string(), MultNode(NumberNode(5), NumberNode(7))._debug_string())

    def test_parse_term_method_div(self):
        parser = Parser([
            Token(TokenType.NUMBER, 5, 1),
            Token(TokenType.FSLASH, 0, 2),
            Token(TokenType.NUMBER, 7, 1),
        ])

        self.assertEqual(parser.parse_term()._debug_string(), DivNode(NumberNode(5), NumberNode(7))._debug_string())

    @unittest.skip('Not implemented yet')
    def test_parse_term_method_eof(self):
        parser = Parser([])

        print(parser.parse_term()._debug_string())

    def test_parse_term_method_not_term_thing(self):
        parser = Parser([
            Token(TokenType.NUMBER, 9, 1),
            Token(TokenType.PLUS, 0, 1),
            Token(TokenType.NUMBER, 9, 1),
        ])

        self.assertEqual(parser.parse_term()._debug_string(), NumberNode(9)._debug_string())

    def test_parse_expr_method_plus(self):
        parser = Parser([
            Token(TokenType.NUMBER, 9, 1),
            Token(TokenType.PLUS, 0, 1),
            Token(TokenType.NUMBER, 9, 1),
        ])

        self.assertEqual(parser.parse_expr()._debug_string(), AddNode(NumberNode(9), NumberNode(9))._debug_string())

    def test_parse_expr_method_minus(self):
        parser = Parser([
            Token(TokenType.NUMBER, 9, 1),
            Token(TokenType.MINUS, 0, 1),
            Token(TokenType.NUMBER, 9, 1),
        ])

        self.assertEqual(parser.parse_expr()._debug_string(), SubNode(NumberNode(9), NumberNode(9))._debug_string())
