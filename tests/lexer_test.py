import unittest

from project.internal_token import TokenType, Token
from project.lexer import Lexer

class LexerTest(unittest.TestCase):
    def test_instantiate_object(self):
        lexer = Lexer('10+10')
        self.assertTrue(lexer)

    def test_peek_method(self):
        lexer = Lexer('43+25')
        self.assertEqual(lexer._peek(), '4')
        lexer.index = 3
        self.assertEqual(lexer._peek(), '2')

    def test_eol_method(self):
        lexer = Lexer('78*46')
        self.assertFalse(lexer._eol())
        lexer.index = 4
        self.assertTrue(lexer._eol())

    def test_eol_edge_case(self):
        lexer = Lexer('')
        self.assertTrue(lexer._eol())

    def test_consume_method(self):
        lexer = Lexer('80*45')
        self.assertEqual(lexer._consume(), '8')
        self.assertEqual(lexer.index, 1)

        lexer.index = 4
        self.assertEqual(lexer._consume(), '5')
        self.assertEqual(lexer.index, 4)

    def test_is_peek_digit_method(self):
        lexer = Lexer('801-67')
        self.assertTrue(lexer._is_peek_digit())
        lexer.index = 3
        self.assertFalse(lexer._is_peek_digit())

    def test_add_token_method(self):
        lexer = Lexer('10+10')
        lexer._add_token(TokenType.NUMBER, 100, 1)
        self.assertEqual(lexer.result, [Token(TokenType.NUMBER, 100, 1)])

    def test_tokens_method(self):
        lexer = Lexer('100')
        self.assertEqual(lexer.tokens(), [
            Token(TokenType.NUMBER, 100, 1)
        ])


    def test_tokens_simple_expression(self):
        lexer = Lexer('123+89')
        self.assertEqual(lexer.tokens(), [
            Token(TokenType.NUMBER, 123, 1),
            Token(TokenType.PLUS, 0, 4),
            Token(TokenType.NUMBER, 89, 5),
        ])

    def test_tokens_symbol(self):
        lexer = Lexer('+-/*()')
        self.assertEqual(lexer.tokens(), [
            Token(TokenType.PLUS, 0, 1),
            Token(TokenType.MINUS, 0, 2),
            Token(TokenType.FSLASH, 0, 3),
            Token(TokenType.ASTERISK, 0, 4),
            Token(TokenType.LPAREN, 0, 5),
            Token(TokenType.RPAREN, 0, 6)
        ])

    @unittest.skip('Not implemented yet')
    def test_tokens_empty(self):
        lexer = Lexer('')
        self.assertEqual(lexer.tokens(), [])
