import unittest

from project.parser import AstNode, NumberNode, Parser
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

    # TODO: test unhandled method
