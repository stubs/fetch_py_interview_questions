

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app42.us.archive.org';archive_analytics.values.server_ms=743;

__wbhack.init('https://web.archive.org/web');




The Spot Game







 The Spot Game 

The game of Spot is played on an NxN board as shown below for N = 4.
During the game, alternate players may either place a black counter
(spot) in an empty square or remove one from the board, thus producing
a variety of patterns. If a board pattern (or its rotation by
90 degrees or 180 degrees) is repeated during a game, the player
producing that pattern loses and the other player wins. The game
terminates in a draw after 2N moves if no duplicate pattern is
produced before then.

Consider the following patterns:

  

If the first pattern had been produced earlier, then any of the
following three patterns (plus one other not shown) would terminate
the game, whereas the last one would not.

Input and Output

Input will consist of a series of games, each consisting of the size
of the board, N (2    N    50) followed, on separate lines, by
2N moves, whether they are all necessary or not. Each move will
consist of the coordinates of a square (integers in the range 1..N)
followed by a blank and a character `+' or `-' indicating the addition
or removal of a spot respectively. You may assume that all moves are
legal, that is there will never be an attempt to place a spot on an
occupied square, nor to remove a non-existent spot. Input
will be terminated by a zero (0).


Output will consist of one line for each game indicating which player
won and on which move, or that the game ended in a draw.

Sample input

2
1 1 +
2 2 +
2 2 -
1 2 +
2
1 1 +
2 2 +
1 2 +
2 2 -
0

Sample output

Player 2 wins on move 3
Draw



