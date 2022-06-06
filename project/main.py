from typing import List
import sys

from internal_token import Token

class Lexer:
    def __init__(self, input: str) -> None:
        self.input = input
        self.index = 0

    def tokens(self) -> List[Token]:
        pass

if __name__ == '__main__':
    program_name = sys.argv[0]

    if len(sys.argv) < 2:
        print(f'USAGE: {program_name} <expression>', file=sys.stderr)
        sys.exit(1)

    input = sys.argv[1]

    tokens = Lexer(input).tokens()
