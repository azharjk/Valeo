from enum import Enum, auto
from typing import List

from project.internal_token import Token, TokenType
# from internal_token import Token, TokenType

class StateType(Enum):
    BEGIN = auto()
    NUMBER = auto()
    SYMBOL = auto()
    EOL = auto()

class Lexer:
    def __init__(self, input: str) -> None:
        self.input = input
        self.index = 0
        self.state = StateType.BEGIN
        self.result: List[Token] = []

    def _peek(self) -> str:
        return self.input[self.index]

    def _eol(self) -> bool:
        return self.index >= len(self.input) - 1

    def _consume(self) -> str:
        ret = self.input[self.index]
        if not self._eol():
            self.index += 1
        return ret

    def _is_peek_digit(self) -> bool:
        return self._peek().isdigit()

    def _add_token(self, token_type: TokenType, value: int, location: int) -> None:
        self.result.append(Token(token_type, value, location))

    def tokens(self) -> List[Token]:
        number_buffer = ''

        while True:
            if self.state == StateType.BEGIN:
                if self._is_peek_digit():
                    self.state = StateType.NUMBER
                else:
                    self.state = StateType.SYMBOL

            elif self.state == StateType.NUMBER:
                if not self._is_peek_digit():
                    self._add_token(TokenType.NUMBER, int(number_buffer), self.index + 1 - len(number_buffer))
                    number_buffer = ''
                    self.state = StateType.SYMBOL
                    continue

                if self._eol():
                    if self._is_peek_digit():
                        number_buffer += self._consume()
                    self._add_token(TokenType.NUMBER, int(number_buffer), self.index + 2 - len(number_buffer))
                    self.state = StateType.EOL

                number_buffer += self._consume()

            elif self.state == StateType.SYMBOL:
                if self._peek() == '+':
                    self._add_token(TokenType.PLUS, 0, self.index + 1)
                elif self._peek() == '-':
                    self._add_token(TokenType.MINUS, 0, self.index + 1)
                elif self._peek() == '*':
                    self._add_token(TokenType.ASTERISK, 0, self.index + 1)
                elif self._peek() == '/':
                    self._add_token(TokenType.FSLASH, 0, self.index + 1)
                elif self._peek() == '(':
                    self._add_token(TokenType.LPAREN, 0, self.index + 1)
                elif self._peek() == ')':
                    self._add_token(TokenType.RPAREN, 0, self.index + 1)
                else:
                    self.state = StateType.NUMBER
                    continue

                if self._eol():
                    self.state = StateType.EOL

                self._consume()

            elif self.state == StateType.EOL:
                break

        return self.result
