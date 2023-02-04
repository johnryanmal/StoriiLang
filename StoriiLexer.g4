lexer grammar StoriiLexer;

options {
	language = Python3;
}

tokens {
	INDENT,
	DEDENT
}

@lexer::header {
from antlr_denter.DenterHelper import DenterHelper
from StoriiParser import StoriiParser
}

@lexer::members {
class StoriiDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: StoriiLexer = lexer

    def pull_token(self):
        return super(StoriiLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.StoriiDenter(self, self.NL, StoriiParser.INDENT, StoriiParser.DEDENT, False)
    return self.denter.next_token()
}

NL: ('\r'? '\n' [ \t]* | 'NL')+;
INDENT: 'INDENT\n';
DEDENT: 'DEDENT\n';

PAREN_L: '(';
PAREN_R: ')';
BRACKET_L: '[';
BRACKET_R: ']';
BRACE_L: '{';
BRACE_R: '}';
ANGLE_L: '<';
ANGLE_R: '>';

SPIKE: '>>';
ARROW: '->';
BAR: '--';
GATE: '==';

WORD: [a-zA-Z_0-9.?!]+;
WS: [ \t\r\f]+ -> skip;