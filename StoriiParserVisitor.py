# Generated from StoriiParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .StoriiParser import StoriiParser
else:
    from StoriiParser import StoriiParser

# This class defines a complete generic visitor for a parse tree produced by StoriiParser.

class StoriiParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StoriiParser#program.
    def visitProgram(self, ctx:StoriiParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#proc.
    def visitProc(self, ctx:StoriiParser.ProcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#block.
    def visitBlock(self, ctx:StoriiParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#system.
    def visitSystem(self, ctx:StoriiParser.SystemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#gate.
    def visitGate(self, ctx:StoriiParser.GateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#room.
    def visitRoom(self, ctx:StoriiParser.RoomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#path.
    def visitPath(self, ctx:StoriiParser.PathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#stmt.
    def visitStmt(self, ctx:StoriiParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#link.
    def visitLink(self, ctx:StoriiParser.LinkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#header.
    def visitHeader(self, ctx:StoriiParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#label.
    def visitLabel(self, ctx:StoriiParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#sub.
    def visitSub(self, ctx:StoriiParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#goto.
    def visitGoto(self, ctx:StoriiParser.GotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#title.
    def visitTitle(self, ctx:StoriiParser.TitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#words.
    def visitWords(self, ctx:StoriiParser.WordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#split.
    def visitSplit(self, ctx:StoriiParser.SplitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#fork.
    def visitFork(self, ctx:StoriiParser.ForkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#spur.
    def visitSpur(self, ctx:StoriiParser.SpurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StoriiParser#main.
    def visitMain(self, ctx:StoriiParser.MainContext):
        return self.visitChildren(ctx)



del StoriiParser