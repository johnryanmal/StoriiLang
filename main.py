import sys
from antlr4 import *
from antlr.StoriiLexer import StoriiLexer
from antlr.StoriiParser import StoriiParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = StoriiLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = StoriiParser(stream)
    tree = parser.startRule()
    print(tree)


if __name__ == '__main__':
    main(sys.argv)
