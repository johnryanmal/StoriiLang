# Generated from StoriiParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .StoriiParser import StoriiParser
else:
    from StoriiParser import StoriiParser

# This class defines a complete listener for a parse tree produced by StoriiParser.
class StoriiParserListener(ParseTreeListener):

    # Enter a parse tree produced by StoriiParser#program.
    def enterProgram(self, ctx:StoriiParser.ProgramContext):
        pass

    # Exit a parse tree produced by StoriiParser#program.
    def exitProgram(self, ctx:StoriiParser.ProgramContext):
        pass


    # Enter a parse tree produced by StoriiParser#stmt.
    def enterStmt(self, ctx:StoriiParser.StmtContext):
        pass

    # Exit a parse tree produced by StoriiParser#stmt.
    def exitStmt(self, ctx:StoriiParser.StmtContext):
        pass


    # Enter a parse tree produced by StoriiParser#node.
    def enterNode(self, ctx:StoriiParser.NodeContext):
        pass

    # Exit a parse tree produced by StoriiParser#node.
    def exitNode(self, ctx:StoriiParser.NodeContext):
        pass


    # Enter a parse tree produced by StoriiParser#label.
    def enterLabel(self, ctx:StoriiParser.LabelContext):
        pass

    # Exit a parse tree produced by StoriiParser#label.
    def exitLabel(self, ctx:StoriiParser.LabelContext):
        pass


    # Enter a parse tree produced by StoriiParser#link.
    def enterLink(self, ctx:StoriiParser.LinkContext):
        pass

    # Exit a parse tree produced by StoriiParser#link.
    def exitLink(self, ctx:StoriiParser.LinkContext):
        pass


    # Enter a parse tree produced by StoriiParser#name.
    def enterName(self, ctx:StoriiParser.NameContext):
        pass

    # Exit a parse tree produced by StoriiParser#name.
    def exitName(self, ctx:StoriiParser.NameContext):
        pass



del StoriiParser