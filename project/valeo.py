from project.lexer import Lexer
from project.parser import Parser

def valeo_eval(input: str) -> float:
    if len(input) == 0:
        return

    tokens = Lexer(input).tokens()
    result = Parser(tokens).parse()

    return result.eval()

def valeo_debug_string(input: str) -> str:
    if len(input) == 0:
        return

    tokens = Lexer(input).tokens()
    result = Parser(tokens).parse()

    return result._debug_string()
