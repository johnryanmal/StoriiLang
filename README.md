# StoriiLang
A computer language for generating interactive fiction.

### Sample based on [Cloak of Darkness](https://www.ifwiki.org/Cloak_of_Darkness)
```
[START]
Intro
{Foyer of the Opera House}
-> south INDENT <Bar> DEDENT
-> west INDENT <Cloakroom> DEDENT
-> north
	<Unusable>
	==
	[Unusable]
	-> first
		Unusable?
	->
		Unusable
==
{Cloakroom}
-> cloak
	Hang cloak?
->
	Take cloak?
<Foyer of the Opera House>
==
{Bar}
-> cloak
	<Dark>
-> disturbed
	Lose
->
	Win
<END>
```
