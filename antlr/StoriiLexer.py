# Generated from StoriiLexer.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from StoriiParser import StoriiParser


def serializedATN():
    return [
        4,0,18,82,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,
        1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,
        1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,
        4,14,72,8,14,11,14,12,14,73,1,15,4,15,77,8,15,11,15,12,15,78,1,15,
        1,15,0,0,16,1,3,3,4,5,5,7,6,9,7,11,8,13,9,15,10,17,11,19,12,21,13,
        23,14,25,15,27,16,29,17,31,18,1,0,2,4,0,48,57,65,90,95,95,97,122,
        3,0,9,9,12,13,32,32,83,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,
        0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,
        0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,1,33,1,0,0,0,3,35,1,0,0,0,5,37,1,
        0,0,0,7,39,1,0,0,0,9,41,1,0,0,0,11,43,1,0,0,0,13,45,1,0,0,0,15,47,
        1,0,0,0,17,49,1,0,0,0,19,51,1,0,0,0,21,54,1,0,0,0,23,57,1,0,0,0,
        25,60,1,0,0,0,27,66,1,0,0,0,29,71,1,0,0,0,31,76,1,0,0,0,33,34,5,
        10,0,0,34,2,1,0,0,0,35,36,5,40,0,0,36,4,1,0,0,0,37,38,5,41,0,0,38,
        6,1,0,0,0,39,40,5,91,0,0,40,8,1,0,0,0,41,42,5,93,0,0,42,10,1,0,0,
        0,43,44,5,123,0,0,44,12,1,0,0,0,45,46,5,125,0,0,46,14,1,0,0,0,47,
        48,5,60,0,0,48,16,1,0,0,0,49,50,5,62,0,0,50,18,1,0,0,0,51,52,5,45,
        0,0,52,53,5,62,0,0,53,20,1,0,0,0,54,55,5,45,0,0,55,56,5,45,0,0,56,
        22,1,0,0,0,57,58,5,61,0,0,58,59,5,61,0,0,59,24,1,0,0,0,60,61,5,83,
        0,0,61,62,5,84,0,0,62,63,5,65,0,0,63,64,5,82,0,0,64,65,5,84,0,0,
        65,26,1,0,0,0,66,67,5,69,0,0,67,68,5,78,0,0,68,69,5,68,0,0,69,28,
        1,0,0,0,70,72,7,0,0,0,71,70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,
        73,74,1,0,0,0,74,30,1,0,0,0,75,77,7,1,0,0,76,75,1,0,0,0,77,78,1,
        0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,80,1,0,0,0,80,81,6,15,0,0,81,
        32,1,0,0,0,3,0,73,78,1,6,0,0
    ]

class StoriiLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    NL = 3
    PAREN_L = 4
    PAREN_R = 5
    BRACKET_L = 6
    BRACKET_R = 7
    BRACE_L = 8
    BRACE_R = 9
    ANGLE_L = 10
    ANGLE_R = 11
    ARROW = 12
    STICK = 13
    GATE = 14
    START = 15
    END = 16
    WORD = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\n'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'<'", "'>'", 
            "'->'", "'--'", "'=='", "'START'", "'END'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PAREN_L", "PAREN_R", "BRACKET_L", 
            "BRACKET_R", "BRACE_L", "BRACE_R", "ANGLE_L", "ANGLE_R", "ARROW", 
            "STICK", "GATE", "START", "END", "WORD", "WS" ]

    ruleNames = [ "NL", "PAREN_L", "PAREN_R", "BRACKET_L", "BRACKET_R", 
                  "BRACE_L", "BRACE_R", "ANGLE_L", "ANGLE_R", "ARROW", "STICK", 
                  "GATE", "START", "END", "WORD", "WS" ]

    grammarFileName = "StoriiLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class StoriiDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: StoriiLexer = lexer

        def pull_token(self):
            return super(StoriiLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.StoriiDenter(self, self.NL, StoriiParser.INDENT, StoriiParser.DEDENT, True)
        return self.denter.next_token()


