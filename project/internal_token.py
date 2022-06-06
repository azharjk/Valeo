from dataclasses import dataclass
from enum import Enum, auto

class TokenType(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    ASTERISK = auto()
    FSLASH = auto()
    LPAREN = auto()
    RPAREN = auto()

@dataclass
class Token:
    type: TokenType
    value: int
    location: int
