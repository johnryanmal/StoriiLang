# Generated from StoriiParser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,26,8,1,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,4,5,41,8,5,11,5,12,5,
        42,1,5,0,0,6,0,2,4,6,8,10,0,0,42,0,12,1,0,0,0,2,25,1,0,0,0,4,27,
        1,0,0,0,6,31,1,0,0,0,8,35,1,0,0,0,10,40,1,0,0,0,12,13,3,2,1,0,13,
        14,5,3,0,0,14,15,1,0,0,0,15,16,3,2,1,0,16,17,5,3,0,0,17,18,1,0,0,
        0,18,19,3,2,1,0,19,20,5,3,0,0,20,1,1,0,0,0,21,26,3,4,2,0,22,26,3,
        6,3,0,23,26,3,8,4,0,24,26,3,10,5,0,25,21,1,0,0,0,25,22,1,0,0,0,25,
        23,1,0,0,0,25,24,1,0,0,0,26,3,1,0,0,0,27,28,5,8,0,0,28,29,3,10,5,
        0,29,30,5,9,0,0,30,5,1,0,0,0,31,32,5,6,0,0,32,33,3,10,5,0,33,34,
        5,7,0,0,34,7,1,0,0,0,35,36,5,10,0,0,36,37,3,10,5,0,37,38,5,11,0,
        0,38,9,1,0,0,0,39,41,5,17,0,0,40,39,1,0,0,0,41,42,1,0,0,0,42,40,
        1,0,0,0,42,43,1,0,0,0,43,11,1,0,0,0,2,25,42
    ]

class StoriiParser ( Parser ):

    grammarFileName = "StoriiParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'\\n'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "'<'", "'>'", "'->'", 
                     "'--'", "'=='", "'START'", "'END'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "NL", "PAREN_L", 
                      "PAREN_R", "BRACKET_L", "BRACKET_R", "BRACE_L", "BRACE_R", 
                      "ANGLE_L", "ANGLE_R", "ARROW", "STICK", "GATE", "START", 
                      "END", "WORD", "WS" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_node = 2
    RULE_label = 3
    RULE_link = 4
    RULE_name = 5

    ruleNames =  [ "program", "stmt", "node", "label", "link", "name" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    NL=3
    PAREN_L=4
    PAREN_R=5
    BRACKET_L=6
    BRACKET_R=7
    BRACE_L=8
    BRACE_R=9
    ANGLE_L=10
    ANGLE_R=11
    ARROW=12
    STICK=13
    GATE=14
    START=15
    END=16
    WORD=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoriiParser.StmtContext)
            else:
                return self.getTypedRuleContext(StoriiParser.StmtContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(StoriiParser.NL)
            else:
                return self.getToken(StoriiParser.NL, i)

        def getRuleIndex(self):
            return StoriiParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = StoriiParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.stmt()
            self.state = 13
            self.match(StoriiParser.NL)

            self.state = 15
            self.stmt()
            self.state = 16
            self.match(StoriiParser.NL)

            self.state = 18
            self.stmt()
            self.state = 19
            self.match(StoriiParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def node(self):
            return self.getTypedRuleContext(StoriiParser.NodeContext,0)


        def label(self):
            return self.getTypedRuleContext(StoriiParser.LabelContext,0)


        def link(self):
            return self.getTypedRuleContext(StoriiParser.LinkContext,0)


        def name(self):
            return self.getTypedRuleContext(StoriiParser.NameContext,0)


        def getRuleIndex(self):
            return StoriiParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = StoriiParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.node()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.label()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.link()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.name()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACE_L(self):
            return self.getToken(StoriiParser.BRACE_L, 0)

        def name(self):
            return self.getTypedRuleContext(StoriiParser.NameContext,0)


        def BRACE_R(self):
            return self.getToken(StoriiParser.BRACE_R, 0)

        def getRuleIndex(self):
            return StoriiParser.RULE_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode" ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode" ):
                listener.exitNode(self)




    def node(self):

        localctx = StoriiParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(StoriiParser.BRACE_L)
            self.state = 28
            self.name()
            self.state = 29
            self.match(StoriiParser.BRACE_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_L(self):
            return self.getToken(StoriiParser.BRACKET_L, 0)

        def name(self):
            return self.getTypedRuleContext(StoriiParser.NameContext,0)


        def BRACKET_R(self):
            return self.getToken(StoriiParser.BRACKET_R, 0)

        def getRuleIndex(self):
            return StoriiParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = StoriiParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(StoriiParser.BRACKET_L)
            self.state = 32
            self.name()
            self.state = 33
            self.match(StoriiParser.BRACKET_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANGLE_L(self):
            return self.getToken(StoriiParser.ANGLE_L, 0)

        def name(self):
            return self.getTypedRuleContext(StoriiParser.NameContext,0)


        def ANGLE_R(self):
            return self.getToken(StoriiParser.ANGLE_R, 0)

        def getRuleIndex(self):
            return StoriiParser.RULE_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink" ):
                listener.enterLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink" ):
                listener.exitLink(self)




    def link(self):

        localctx = StoriiParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(StoriiParser.ANGLE_L)
            self.state = 36
            self.name()
            self.state = 37
            self.match(StoriiParser.ANGLE_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(StoriiParser.WORD)
            else:
                return self.getToken(StoriiParser.WORD, i)

        def getRuleIndex(self):
            return StoriiParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = StoriiParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self.match(StoriiParser.WORD)
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==17):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





