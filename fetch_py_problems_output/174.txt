

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app42.us.archive.org';archive_analytics.values.server_ms=552;

__wbhack.init('https://web.archive.org/web');




Strategy







 Strategy 

A well known psychology experiment involves people playing a game in
which they can either trade with each other or attempt to cheat the
other player. If both players TRADE then each gains one point. If one
TRADEs and the other CHEATs then the TRADEr loses 2 points and the
CHEATer wins 2. If both CHEAT then each loses 1 point.


There are a variety of different strategies for playing this game,
although most people are either unable to find a winning strategy, or,
having decided on a strategy, do not stick to it. Thus it is fairer to
attempt to evaluate these strategies by simulation on a computer. Each
strategy is simulated by an automaton. An automaton is characterised
by a program incorporating the strategy, a memory for previous
encounters and a count reflecting the score of that automaton. The
count starts at zero and is altered according to the above rules after
each encounter. The memory is able to determine what happened on up to
the last two encounters with each other contender.


Write a program that will read in details of up to 10 different
strategies, play each strategy against each other strategy 10 times
and then print out the final scores. Strategies will be in the form of
simple programs obeying the following grammar:

 
<program> ::= <statement>.  
<statement> ::= <command>    <ifstat>  
<ifstat> ::= IF <condition> THEN <statement> ELSE <statement>  
<condition> ::= <cond>    <cond> <op> <condition>  
<op> ::= AND    OR  
<cond> ::= <memory> {=    #} {<command>    NULL}  
<memory> ::= {MY    YOUR} LAST {1    2}  
<command> ::= TRADE    CHEAT


Note that LAST1 refers to the previous encounter between these two
automata, LAST2 to the encounter before that and that `MY' and `YOUR'
have the obvious meanings. Spaces and line breaks may appear anywhere
in the program and are for legibility only. The symbol `#' means `is
not equal to'. NULL indicates that an encounter has not ocurred.  The
following are valid programs:

CHEAT.
IF MY LAST1 = CHEAT THEN TRADE ELSE CHEAT.
IFYOURLAST2=NULLTHENTRADEELSEIFYOURLAST1=TRADETHENTRADE
ELSECHEAT.

Input

Input will consist of a series of programs. Each program will be no
longer than 255 characters and may be split over several lines for
convenience. There will be no more than 10 programs. The file will be
terminated by a line containing only a single `#'.

Output

Output will consist of one line for each line of input. Each line will
consist of the final score of the relevant program right justified in
a field of width 3.

Sample input

CHEAT.
IF MY LAST1 = CHEAT THEN TRADE ELSE CHEAT.
IFYOURLAST2=NULLTHENTRADEELSEIFYOURLAST1=TRADETHENTRADE
ELSECHEAT.
#

Sample output

  1
-12
-13



