import sys

from lexer import Lexer

if __name__ == '__main__':
    program_name = sys.argv[0]

    if len(sys.argv) < 2:
        print(f'USAGE: {program_name} <expression>', file=sys.stderr)
        sys.exit(1)

    input = sys.argv[1]

    tokens = Lexer(input).tokens()
    print(tokens)
