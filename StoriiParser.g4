parser grammar StoriiParser;

options {
	language = Python3;
	tokenVocab = StoriiLexer;
}

program: system;

proc: NL | block;
block: INDENT system DEDENT;
system: gate* room (gate room)* gate*;
gate: '==' NL;

room: (path | split)+;

path: stmt+;
stmt: link NL;
link: header | label | sub | goto | title;
header: '{' name '}';
label: '[' name ']';
sub: '(' name ')';
goto: '<' name '>';
title: name;
name: WORD+;

split: (fork | spur)+ main?;
fork: '->' WORD? proc;
spur: '>>' WORD? proc;
main: '--' proc;
