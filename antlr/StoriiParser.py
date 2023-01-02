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
        4,1,17,134,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,1,1,1,3,1,41,8,
        1,1,2,1,2,1,2,1,2,1,3,5,3,48,8,3,10,3,12,3,51,9,3,1,3,1,3,1,3,1,
        3,5,3,57,8,3,10,3,12,3,60,9,3,1,3,5,3,63,8,3,10,3,12,3,66,9,3,1,
        4,1,4,1,4,1,5,1,5,4,5,73,8,5,11,5,12,5,74,1,6,4,6,78,8,6,11,6,12,
        6,79,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,89,8,8,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,13,4,13,106,8,13,
        11,13,12,13,107,1,14,1,14,4,14,112,8,14,11,14,12,14,113,1,14,3,14,
        117,8,14,1,15,1,15,3,15,121,8,15,1,15,1,15,1,16,1,16,3,16,127,8,
        16,1,16,1,16,1,17,1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,0,0,131,0,36,1,0,0,0,2,40,1,0,0,0,4,42,1,
        0,0,0,6,49,1,0,0,0,8,67,1,0,0,0,10,72,1,0,0,0,12,77,1,0,0,0,14,81,
        1,0,0,0,16,88,1,0,0,0,18,90,1,0,0,0,20,94,1,0,0,0,22,98,1,0,0,0,
        24,102,1,0,0,0,26,105,1,0,0,0,28,111,1,0,0,0,30,118,1,0,0,0,32,124,
        1,0,0,0,34,130,1,0,0,0,36,37,3,6,3,0,37,1,1,0,0,0,38,41,5,3,0,0,
        39,41,3,4,2,0,40,38,1,0,0,0,40,39,1,0,0,0,41,3,1,0,0,0,42,43,5,1,
        0,0,43,44,3,6,3,0,44,45,5,2,0,0,45,5,1,0,0,0,46,48,3,8,4,0,47,46,
        1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,
        51,49,1,0,0,0,52,58,3,10,5,0,53,54,3,8,4,0,54,55,3,10,5,0,55,57,
        1,0,0,0,56,53,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,
        59,64,1,0,0,0,60,58,1,0,0,0,61,63,3,8,4,0,62,61,1,0,0,0,63,66,1,
        0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,7,1,0,0,0,66,64,1,0,0,0,67,
        68,5,15,0,0,68,69,5,3,0,0,69,9,1,0,0,0,70,73,3,12,6,0,71,73,3,28,
        14,0,72,70,1,0,0,0,72,71,1,0,0,0,73,74,1,0,0,0,74,72,1,0,0,0,74,
        75,1,0,0,0,75,11,1,0,0,0,76,78,3,14,7,0,77,76,1,0,0,0,78,79,1,0,
        0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,13,1,0,0,0,81,82,3,16,8,0,82,
        83,5,3,0,0,83,15,1,0,0,0,84,89,3,18,9,0,85,89,3,20,10,0,86,89,3,
        22,11,0,87,89,3,24,12,0,88,84,1,0,0,0,88,85,1,0,0,0,88,86,1,0,0,
        0,88,87,1,0,0,0,89,17,1,0,0,0,90,91,5,8,0,0,91,92,3,26,13,0,92,93,
        5,9,0,0,93,19,1,0,0,0,94,95,5,6,0,0,95,96,3,26,13,0,96,97,5,7,0,
        0,97,21,1,0,0,0,98,99,5,10,0,0,99,100,3,26,13,0,100,101,5,11,0,0,
        101,23,1,0,0,0,102,103,3,26,13,0,103,25,1,0,0,0,104,106,5,16,0,0,
        105,104,1,0,0,0,106,107,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,
        108,27,1,0,0,0,109,112,3,30,15,0,110,112,3,32,16,0,111,109,1,0,0,
        0,111,110,1,0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,
        0,114,116,1,0,0,0,115,117,3,34,17,0,116,115,1,0,0,0,116,117,1,0,
        0,0,117,29,1,0,0,0,118,120,5,13,0,0,119,121,5,16,0,0,120,119,1,0,
        0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,123,3,2,1,0,123,31,1,0,0,
        0,124,126,5,12,0,0,125,127,5,16,0,0,126,125,1,0,0,0,126,127,1,0,
        0,0,127,128,1,0,0,0,128,129,3,2,1,0,129,33,1,0,0,0,130,131,5,14,
        0,0,131,132,3,2,1,0,132,35,1,0,0,0,14,40,49,58,64,72,74,79,88,107,
        111,113,116,120,126
    ]

class StoriiParser ( Parser ):

    grammarFileName = "StoriiParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'INDENT\\n'", "'DEDENT\\n'", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "'<'", "'>'", 
                     "'>>'", "'->'", "'--'", "'=='" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "NL", "PAREN_L", 
                      "PAREN_R", "BRACKET_L", "BRACKET_R", "BRACE_L", "BRACE_R", 
                      "ANGLE_L", "ANGLE_R", "SPIKE", "ARROW", "BAR", "GATE", 
                      "WORD", "WS" ]

    RULE_program = 0
    RULE_proc = 1
    RULE_block = 2
    RULE_system = 3
    RULE_gate = 4
    RULE_room = 5
    RULE_path = 6
    RULE_stmt = 7
    RULE_link = 8
    RULE_header = 9
    RULE_label = 10
    RULE_goto = 11
    RULE_title = 12
    RULE_name = 13
    RULE_split = 14
    RULE_fork = 15
    RULE_spur = 16
    RULE_main = 17

    ruleNames =  [ "program", "proc", "block", "system", "gate", "room", 
                   "path", "stmt", "link", "header", "label", "goto", "title", 
                   "name", "split", "fork", "spur", "main" ]

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
    SPIKE=12
    ARROW=13
    BAR=14
    GATE=15
    WORD=16
    WS=17

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

        def system(self):
            return self.getTypedRuleContext(StoriiParser.SystemContext,0)


        def getRuleIndex(self):
            return StoriiParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = StoriiParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.system()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(StoriiParser.NL, 0)

        def block(self):
            return self.getTypedRuleContext(StoriiParser.BlockContext,0)


        def getRuleIndex(self):
            return StoriiParser.RULE_proc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProc" ):
                return visitor.visitProc(self)
            else:
                return visitor.visitChildren(self)




    def proc(self):

        localctx = StoriiParser.ProcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_proc)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(StoriiParser.NL)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.block()
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


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(StoriiParser.INDENT, 0)

        def system(self):
            return self.getTypedRuleContext(StoriiParser.SystemContext,0)


        def DEDENT(self):
            return self.getToken(StoriiParser.DEDENT, 0)

        def getRuleIndex(self):
            return StoriiParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = StoriiParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(StoriiParser.INDENT)
            self.state = 43
            self.system()
            self.state = 44
            self.match(StoriiParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SystemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def room(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoriiParser.RoomContext)
            else:
                return self.getTypedRuleContext(StoriiParser.RoomContext,i)


        def gate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoriiParser.GateContext)
            else:
                return self.getTypedRuleContext(StoriiParser.GateContext,i)


        def getRuleIndex(self):
            return StoriiParser.RULE_system

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSystem" ):
                return visitor.visitSystem(self)
            else:
                return visitor.visitChildren(self)




    def system(self):

        localctx = StoriiParser.SystemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_system)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 46
                self.gate()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.room()
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 53
                    self.gate()
                    self.state = 54
                    self.room() 
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 61
                self.gate()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GATE(self):
            return self.getToken(StoriiParser.GATE, 0)

        def NL(self):
            return self.getToken(StoriiParser.NL, 0)

        def getRuleIndex(self):
            return StoriiParser.RULE_gate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGate" ):
                return visitor.visitGate(self)
            else:
                return visitor.visitChildren(self)




    def gate(self):

        localctx = StoriiParser.GateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_gate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(StoriiParser.GATE)
            self.state = 68
            self.match(StoriiParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def path(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoriiParser.PathContext)
            else:
                return self.getTypedRuleContext(StoriiParser.PathContext,i)


        def split(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoriiParser.SplitContext)
            else:
                return self.getTypedRuleContext(StoriiParser.SplitContext,i)


        def getRuleIndex(self):
            return StoriiParser.RULE_room

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoom" ):
                return visitor.visitRoom(self)
            else:
                return visitor.visitChildren(self)




    def room(self):

        localctx = StoriiParser.RoomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_room)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6, 8, 10, 16]:
                    self.state = 70
                    self.path()
                    pass
                elif token in [12, 13]:
                    self.state = 71
                    self.split()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 79168) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoriiParser.StmtContext)
            else:
                return self.getTypedRuleContext(StoriiParser.StmtContext,i)


        def getRuleIndex(self):
            return StoriiParser.RULE_path

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPath" ):
                return visitor.visitPath(self)
            else:
                return visitor.visitChildren(self)




    def path(self):

        localctx = StoriiParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 76
                    self.stmt()

                else:
                    raise NoViableAltException(self)
                self.state = 79 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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

        def link(self):
            return self.getTypedRuleContext(StoriiParser.LinkContext,0)


        def NL(self):
            return self.getToken(StoriiParser.NL, 0)

        def getRuleIndex(self):
            return StoriiParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = StoriiParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.link()
            self.state = 82
            self.match(StoriiParser.NL)
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

        def header(self):
            return self.getTypedRuleContext(StoriiParser.HeaderContext,0)


        def label(self):
            return self.getTypedRuleContext(StoriiParser.LabelContext,0)


        def goto(self):
            return self.getTypedRuleContext(StoriiParser.GotoContext,0)


        def title(self):
            return self.getTypedRuleContext(StoriiParser.TitleContext,0)


        def getRuleIndex(self):
            return StoriiParser.RULE_link

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLink" ):
                return visitor.visitLink(self)
            else:
                return visitor.visitChildren(self)




    def link(self):

        localctx = StoriiParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_link)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.header()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.label()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.goto()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.title()
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


    class HeaderContext(ParserRuleContext):
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
            return StoriiParser.RULE_header

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader" ):
                return visitor.visitHeader(self)
            else:
                return visitor.visitChildren(self)




    def header(self):

        localctx = StoriiParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(StoriiParser.BRACE_L)
            self.state = 91
            self.name()
            self.state = 92
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = StoriiParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(StoriiParser.BRACKET_L)
            self.state = 95
            self.name()
            self.state = 96
            self.match(StoriiParser.BRACKET_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoContext(ParserRuleContext):
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
            return StoriiParser.RULE_goto

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoto" ):
                return visitor.visitGoto(self)
            else:
                return visitor.visitChildren(self)




    def goto(self):

        localctx = StoriiParser.GotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_goto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(StoriiParser.ANGLE_L)
            self.state = 99
            self.name()
            self.state = 100
            self.match(StoriiParser.ANGLE_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TitleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(StoriiParser.NameContext,0)


        def getRuleIndex(self):
            return StoriiParser.RULE_title

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTitle" ):
                return visitor.visitTitle(self)
            else:
                return visitor.visitChildren(self)




    def title(self):

        localctx = StoriiParser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.name()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = StoriiParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.match(StoriiParser.WORD)
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SplitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fork(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoriiParser.ForkContext)
            else:
                return self.getTypedRuleContext(StoriiParser.ForkContext,i)


        def spur(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StoriiParser.SpurContext)
            else:
                return self.getTypedRuleContext(StoriiParser.SpurContext,i)


        def main(self):
            return self.getTypedRuleContext(StoriiParser.MainContext,0)


        def getRuleIndex(self):
            return StoriiParser.RULE_split

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSplit" ):
                return visitor.visitSplit(self)
            else:
                return visitor.visitChildren(self)




    def split(self):

        localctx = StoriiParser.SplitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_split)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 111
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [13]:
                        self.state = 109
                        self.fork()
                        pass
                    elif token in [12]:
                        self.state = 110
                        self.spur()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 113 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 115
                self.main()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARROW(self):
            return self.getToken(StoriiParser.ARROW, 0)

        def proc(self):
            return self.getTypedRuleContext(StoriiParser.ProcContext,0)


        def WORD(self):
            return self.getToken(StoriiParser.WORD, 0)

        def getRuleIndex(self):
            return StoriiParser.RULE_fork

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFork" ):
                return visitor.visitFork(self)
            else:
                return visitor.visitChildren(self)




    def fork(self):

        localctx = StoriiParser.ForkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_fork)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(StoriiParser.ARROW)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 119
                self.match(StoriiParser.WORD)


            self.state = 122
            self.proc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpurContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPIKE(self):
            return self.getToken(StoriiParser.SPIKE, 0)

        def proc(self):
            return self.getTypedRuleContext(StoriiParser.ProcContext,0)


        def WORD(self):
            return self.getToken(StoriiParser.WORD, 0)

        def getRuleIndex(self):
            return StoriiParser.RULE_spur

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpur" ):
                return visitor.visitSpur(self)
            else:
                return visitor.visitChildren(self)




    def spur(self):

        localctx = StoriiParser.SpurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_spur)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(StoriiParser.SPIKE)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 125
                self.match(StoriiParser.WORD)


            self.state = 128
            self.proc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BAR(self):
            return self.getToken(StoriiParser.BAR, 0)

        def proc(self):
            return self.getTypedRuleContext(StoriiParser.ProcContext,0)


        def getRuleIndex(self):
            return StoriiParser.RULE_main

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = StoriiParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(StoriiParser.BAR)
            self.state = 131
            self.proc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





