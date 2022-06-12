import sys
from typing import List, Union

from project.internal_token import Token, TokenType

class AstNode:
    def _debug_string(self) -> str:
        return 'AstNode::_debug_string()'

    def eval(self) -> float:
        pass

class NumberNode(AstNode):
    def __init__(self, value: int) -> None:
        self.value = value

    def _debug_string(self) -> str:
        return f'{self.value}'

    def eval(self) -> float:
        return self.value

class BinaryOpNode(AstNode):
    def __init__(self, lhs: AstNode, rhs: AstNode) -> None:
        self.lhs = lhs
        self.rhs = rhs

    def _debug_string(self) -> str:
        pass

    def eval(self) -> float:
        pass

class AddNode(BinaryOpNode):
    def _debug_string(self) -> str:
        return f'({self.lhs._debug_string()} + {self.rhs._debug_string()})'

    def eval(self) -> float:
        return self.lhs.eval() + self.rhs.eval()

class SubNode(BinaryOpNode):
    def _debug_string(self) -> str:
        return f'({self.lhs._debug_string()} - {self.rhs._debug_string()})'

    def eval(self) -> float:
        return self.lhs.eval() - self.rhs.eval()

class MultNode(BinaryOpNode):
    def _debug_string(self) -> str:
        return f'({self.lhs._debug_string()} * {self.rhs._debug_string()})'

    def eval(self) -> float:
        return self.lhs.eval() * self.rhs.eval()

class DivNode(BinaryOpNode):
    def _debug_string(self) -> str:
        return f'({self.lhs._debug_string()} / {self.rhs._debug_string()})'

    def eval(self) -> float:
        return self.lhs.eval() / self.rhs.eval()

class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = tokens
        self.index = 0

    def _eof(self) -> bool:
        return self.index >= len(self.tokens) - 1

    def _peek(self) -> Token:
        return self.tokens[self.index]

    def _consume(self) -> Token:
        ret = self._peek()
        if not self._eof():
            self.index += 1
        return ret

    def parse_number(self) -> AstNode:
        token = self._consume()
        assert token.type == TokenType.NUMBER
        return NumberNode(token.value)

    def parse_paren(self) -> AstNode:
        lparen = self._consume()

        assert lparen.type == TokenType.LPAREN
        if self.index >= len(self.tokens):
            print(f'ERROR: expected correct expression but got "{lparen.type}" at location {lparen.location}', file=sys.stderr)
            sys.exit(1)

        expr = self.parse_expr()

        rparen = None
        if not self.index >= len(self.tokens):
            rparen = self._peek()

        if rparen is None or rparen.type != TokenType.RPAREN:
            print(f'ERROR: unclosed parenthesis at location {lparen.location}', file=sys.stderr)
            sys.exit(1)

        self.index += 1

        return expr

    def parse_primary(self) -> AstNode:
        token = self._peek()
        ret = AstNode()
        if token.type == TokenType.NUMBER:
            ret = self.parse_number()
        elif token.type == TokenType.LPAREN:
            ret = self.parse_paren()
        else:
            print(f'ERROR: expected correct expression but got "{token.type}" at location {token.location}', file=sys.stderr)
            sys.exit(1)
        return ret

    def parse_term(self) -> AstNode:
        lhs = self.parse_primary()

        while True:
            if self._eof():
                break

            token = self._peek()
            if token.type == TokenType.ASTERISK:
                self._consume()
                lhs = MultNode(lhs, self.parse_primary())
            elif token.type == TokenType.FSLASH:
                self._consume()
                lhs = DivNode(lhs, self.parse_primary())
            else:
                break

        return lhs

    def parse_expr(self) -> AstNode:
        lhs = self.parse_term()

        while True:
            try:
                token = self._peek()
            except IndexError:
                break

            if token.type == TokenType.PLUS:
                self._consume()
                lhs = AddNode(lhs, self.parse_term())
            elif token.type == TokenType.MINUS:
                self._consume()
                lhs = SubNode(lhs, self.parse_term())
            elif token.type == TokenType.RPAREN:
                break

            if self._eof():
                break

        return lhs

    def parse(self) -> Union[AstNode, None]:
        if len(self.tokens) == 0:
            return None

        return self.parse_expr()
