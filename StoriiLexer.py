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
        4,0,17,107,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,1,0,3,0,37,8,0,1,0,1,0,5,0,
        41,8,0,10,0,12,0,44,9,0,1,0,1,0,4,0,48,8,0,11,0,12,0,49,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,
        11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,15,4,15,97,
        8,15,11,15,12,15,98,1,16,4,16,102,8,16,11,16,12,16,103,1,16,1,16,
        0,0,17,1,3,3,1,5,2,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,
        25,13,27,14,29,15,31,16,33,17,1,0,3,2,0,9,9,32,32,7,0,33,33,46,46,
        48,57,63,63,65,90,95,95,97,122,3,0,9,9,12,13,32,32,112,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,
        13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,
        23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,
        33,1,0,0,0,1,47,1,0,0,0,3,51,1,0,0,0,5,59,1,0,0,0,7,67,1,0,0,0,9,
        69,1,0,0,0,11,71,1,0,0,0,13,73,1,0,0,0,15,75,1,0,0,0,17,77,1,0,0,
        0,19,79,1,0,0,0,21,81,1,0,0,0,23,83,1,0,0,0,25,86,1,0,0,0,27,89,
        1,0,0,0,29,92,1,0,0,0,31,96,1,0,0,0,33,101,1,0,0,0,35,37,5,13,0,
        0,36,35,1,0,0,0,36,37,1,0,0,0,37,38,1,0,0,0,38,42,5,10,0,0,39,41,
        7,0,0,0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,
        43,48,1,0,0,0,44,42,1,0,0,0,45,46,5,78,0,0,46,48,5,76,0,0,47,36,
        1,0,0,0,47,45,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,
        50,2,1,0,0,0,51,52,5,73,0,0,52,53,5,78,0,0,53,54,5,68,0,0,54,55,
        5,69,0,0,55,56,5,78,0,0,56,57,5,84,0,0,57,58,5,10,0,0,58,4,1,0,0,
        0,59,60,5,68,0,0,60,61,5,69,0,0,61,62,5,68,0,0,62,63,5,69,0,0,63,
        64,5,78,0,0,64,65,5,84,0,0,65,66,5,10,0,0,66,6,1,0,0,0,67,68,5,40,
        0,0,68,8,1,0,0,0,69,70,5,41,0,0,70,10,1,0,0,0,71,72,5,91,0,0,72,
        12,1,0,0,0,73,74,5,93,0,0,74,14,1,0,0,0,75,76,5,123,0,0,76,16,1,
        0,0,0,77,78,5,125,0,0,78,18,1,0,0,0,79,80,5,60,0,0,80,20,1,0,0,0,
        81,82,5,62,0,0,82,22,1,0,0,0,83,84,5,62,0,0,84,85,5,62,0,0,85,24,
        1,0,0,0,86,87,5,45,0,0,87,88,5,62,0,0,88,26,1,0,0,0,89,90,5,45,0,
        0,90,91,5,45,0,0,91,28,1,0,0,0,92,93,5,61,0,0,93,94,5,61,0,0,94,
        30,1,0,0,0,95,97,7,1,0,0,96,95,1,0,0,0,97,98,1,0,0,0,98,96,1,0,0,
        0,98,99,1,0,0,0,99,32,1,0,0,0,100,102,7,2,0,0,101,100,1,0,0,0,102,
        103,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,
        106,6,16,0,0,106,34,1,0,0,0,7,0,36,42,47,49,98,103,1,6,0,0
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



