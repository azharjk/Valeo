import sys

from project.lexer import Lexer
from project.parser import AstNode, Parser

def valeo_bootstrap(input: str) -> AstNode:
    if len(input) == 0:
        print('ERROR: please enter an expression', file=sys.stderr)
        sys.exit(1)

    tokens = Lexer(input).tokens()
    result = Parser(tokens).parse()

    if result is None:
        print('ERROR: please enter a valid expression', file=sys.stderr)
        sys.exit(1)

    return result


def valeo_eval(input: str) -> float:
    result = valeo_bootstrap(input)
    return result.eval()

def valeo_debug_string(input: str) -> str:
    result = valeo_bootstrap(input)
    return result._debug_string()
