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
        4,0,17,104,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,5,0,38,8,0,10,0,12,
        0,41,9,0,1,0,1,0,4,0,45,8,0,11,0,12,0,46,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,
        1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,12,1,
        12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,15,4,15,94,8,15,11,15,12,
        15,95,1,16,4,16,99,8,16,11,16,12,16,100,1,16,1,16,0,0,17,1,3,3,1,
        5,2,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,
        15,31,16,33,17,1,0,2,7,0,33,33,46,46,48,57,63,63,65,90,95,95,97,
        122,3,0,9,9,12,13,32,32,108,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,
        27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,1,44,1,0,0,0,3,
        48,1,0,0,0,5,56,1,0,0,0,7,64,1,0,0,0,9,66,1,0,0,0,11,68,1,0,0,0,
        13,70,1,0,0,0,15,72,1,0,0,0,17,74,1,0,0,0,19,76,1,0,0,0,21,78,1,
        0,0,0,23,80,1,0,0,0,25,83,1,0,0,0,27,86,1,0,0,0,29,89,1,0,0,0,31,
        93,1,0,0,0,33,98,1,0,0,0,35,39,5,10,0,0,36,38,5,32,0,0,37,36,1,0,
        0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,45,1,0,0,0,41,39,
        1,0,0,0,42,43,5,78,0,0,43,45,5,76,0,0,44,35,1,0,0,0,44,42,1,0,0,
        0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,2,1,0,0,0,48,49,5,
        73,0,0,49,50,5,78,0,0,50,51,5,68,0,0,51,52,5,69,0,0,52,53,5,78,0,
        0,53,54,5,84,0,0,54,55,5,10,0,0,55,4,1,0,0,0,56,57,5,68,0,0,57,58,
        5,69,0,0,58,59,5,68,0,0,59,60,5,69,0,0,60,61,5,78,0,0,61,62,5,84,
        0,0,62,63,5,10,0,0,63,6,1,0,0,0,64,65,5,40,0,0,65,8,1,0,0,0,66,67,
        5,41,0,0,67,10,1,0,0,0,68,69,5,91,0,0,69,12,1,0,0,0,70,71,5,93,0,
        0,71,14,1,0,0,0,72,73,5,123,0,0,73,16,1,0,0,0,74,75,5,125,0,0,75,
        18,1,0,0,0,76,77,5,60,0,0,77,20,1,0,0,0,78,79,5,62,0,0,79,22,1,0,
        0,0,80,81,5,62,0,0,81,82,5,62,0,0,82,24,1,0,0,0,83,84,5,45,0,0,84,
        85,5,62,0,0,85,26,1,0,0,0,86,87,5,45,0,0,87,88,5,45,0,0,88,28,1,
        0,0,0,89,90,5,61,0,0,90,91,5,61,0,0,91,30,1,0,0,0,92,94,7,0,0,0,
        93,92,1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,32,1,
        0,0,0,97,99,7,1,0,0,98,97,1,0,0,0,99,100,1,0,0,0,100,98,1,0,0,0,
        100,101,1,0,0,0,101,102,1,0,0,0,102,103,6,16,0,0,103,34,1,0,0,0,
        6,0,39,44,46,95,100,1,6,0,0
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
    SPIKE = 12
    ARROW = 13
    BAR = 14
    GATE = 15
    WORD = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'INDENT\\n'", "'DEDENT\\n'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "'<'", "'>'", "'>>'", "'->'", "'--'", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PAREN_L", "PAREN_R", "BRACKET_L", 
            "BRACKET_R", "BRACE_L", "BRACE_R", "ANGLE_L", "ANGLE_R", "SPIKE", 
            "ARROW", "BAR", "GATE", "WORD", "WS" ]

    ruleNames = [ "NL", "INDENT", "DEDENT", "PAREN_L", "PAREN_R", "BRACKET_L", 
                  "BRACKET_R", "BRACE_L", "BRACE_R", "ANGLE_L", "ANGLE_R", 
                  "SPIKE", "ARROW", "BAR", "GATE", "WORD", "WS" ]

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



