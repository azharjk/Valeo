import sys

from project.lexer import Lexer
from project.parser import Parser
from project.valeo import valeo_debug_string, valeo_eval

if __name__ == '__main__':
    program_name = sys.argv[0]

    if len(sys.argv) < 2:
        print(f'USAGE: {program_name} <expression>', file=sys.stderr)
        sys.exit(1)

    input = sys.argv[1]

    if len(input) == 0:
        sys.exit(0)

    tokens = Lexer(input).tokens()
    print('[TOKENS]: ')
    print(tokens)
    print()

    result = Parser(tokens).parse()
    print('[DEBUG_STRING]: ')
    print(valeo_debug_string(input))
    print()

    print('[RESULT_EVAL]: ')
    print(valeo_eval(input))
