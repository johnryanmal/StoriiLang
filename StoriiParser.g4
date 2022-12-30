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

path: page+;
page: node NL;
node: header | label | link | title;
header: '{' name '}';
label: '[' name ']';
link: '<' name '>';
title: name;
name: WORD+;

split: (fork | spur)+ main?;
fork: '->' WORD? proc;
spur: '>>' WORD? proc;
main: '--' proc;
