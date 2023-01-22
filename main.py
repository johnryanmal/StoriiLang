import sys
from antlr4 import *
from StoriiLexer import StoriiLexer
from StoriiParser import StoriiParser
from StoriiVisitor import StoriiVisitor


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = StoriiLexer(input_stream)
    #print(list(lexer.symbolicNames[token.type] for token in lexer.getAllTokens()))
    stream = CommonTokenStream(lexer)
    parser = StoriiParser(stream)
    tree = parser.program()
    visitor = StoriiVisitor()
    ast = visitor.visitProgram(tree)
    print(ast)


if __name__ == '__main__':
    main(sys.argv)
