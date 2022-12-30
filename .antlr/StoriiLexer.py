# Generated from /Users/johnryan/Documents/Repos/Storii/StoriiLexer.g4 by ANTLR 4.9.2
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
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\2\6\2)\n\2\r\2\16\2*\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\6\21Z\n\21\r\21\16\21[\3\22\6\22_\n\22\r\22\16\22`\3")
        buf.write("\22\3\22\2\2\23\3\5\5\3\7\4\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23\3\2\4\t")
        buf.write("\2##\60\60\62;AAC\\aac|\5\2\13\13\16\17\"\"\2g\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3(\3\2\2\2")
        buf.write("\5,\3\2\2\2\7\64\3\2\2\2\t<\3\2\2\2\13>\3\2\2\2\r@\3\2")
        buf.write("\2\2\17B\3\2\2\2\21D\3\2\2\2\23F\3\2\2\2\25H\3\2\2\2\27")
        buf.write("J\3\2\2\2\31L\3\2\2\2\33O\3\2\2\2\35R\3\2\2\2\37U\3\2")
        buf.write("\2\2!Y\3\2\2\2#^\3\2\2\2%)\7\f\2\2&\'\7P\2\2\')\7N\2\2")
        buf.write("(%\3\2\2\2(&\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\4")
        buf.write("\3\2\2\2,-\7K\2\2-.\7P\2\2./\7F\2\2/\60\7G\2\2\60\61\7")
        buf.write("P\2\2\61\62\7V\2\2\62\63\7\f\2\2\63\6\3\2\2\2\64\65\7")
        buf.write("F\2\2\65\66\7G\2\2\66\67\7F\2\2\678\7G\2\289\7P\2\29:")
        buf.write("\7V\2\2:;\7\f\2\2;\b\3\2\2\2<=\7*\2\2=\n\3\2\2\2>?\7+")
        buf.write("\2\2?\f\3\2\2\2@A\7]\2\2A\16\3\2\2\2BC\7_\2\2C\20\3\2")
        buf.write("\2\2DE\7}\2\2E\22\3\2\2\2FG\7\177\2\2G\24\3\2\2\2HI\7")
        buf.write(">\2\2I\26\3\2\2\2JK\7@\2\2K\30\3\2\2\2LM\7@\2\2MN\7@\2")
        buf.write("\2N\32\3\2\2\2OP\7/\2\2PQ\7@\2\2Q\34\3\2\2\2RS\7/\2\2")
        buf.write("ST\7/\2\2T\36\3\2\2\2UV\7?\2\2VW\7?\2\2W \3\2\2\2XZ\t")
        buf.write("\2\2\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\\"\3")
        buf.write("\2\2\2]_\t\3\2\2^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2")
        buf.write("\2ab\3\2\2\2bc\b\22\2\2c$\3\2\2\2\7\2(*[`\3\b\2\2")
        return buf.getvalue()


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
            "'INDENT\n'", "'DEDENT\n'", "'('", "')'", "'['", "']'", "'{'", 
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
        self.checkVersion("4.9.2")
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



