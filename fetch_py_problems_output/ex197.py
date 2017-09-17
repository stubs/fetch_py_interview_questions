

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app17.us.archive.org';archive_analytics.values.server_ms=521;

__wbhack.init('https://web.archive.org/web');




Cube










 
Cube 


There was once a 3 by 3 by 3 cube built of 27 smaller cubes. It has fallen
apart into seven pieces: 





Figure 1:
The seven pieces that once formed a cube




The seven pieces can be assembled in many ways to again form the cube. Figure
2 shows one of these possibilities. The first square stands for the front
plane, the next one for the middle plane and the last one for the back plane
of the cube. The letters in the cells stand for the name of piece filling
out the corresponding space in the cube. The name of the seven pieces can
be found in figure 1.





Figure 2:
Two possibilities of assembling the cube




You are to write a program that outputs all possibilities of assembling
the cube but suppress solutions that are mere rotations of another solution.




Hint:
Piece a is the only part that, by rotation and translation, cannot
be transformed into itself. In order to avoid solutions that are mere rotations
of an already found solution, you may restrict transformations of piece
a to translations. 



Input 

The input file has several test cases. Each test case indicates
the initial position of piece `a'. You can translate it, but you
mustn't rotate it.



Output 

For each solution found, your program should output a line containing the
solution as a string. The string is a linearized form of the cube. Each
letter stands for the piece filling out the corresponding space in the cube.
It is linearized as follows: 


The string consists of substrings representing the front, middle and
back plane. 

Each substring consists of substrings representing the top, middle and
bottom row. 

Each row substring consists of letters representing the left, middle
and right cell. 


The solutions in figure 2 would be represented like this: 

adcaccaacddgbfgffedggbfebee
aababbadcffegfcddcfeeggedgc


It is very important that your program uses the naming convention given
in figure 1 and linearizes the cube as explained above.


Print a blank line after each test case. 





Figure 3:
Positions of the cells in the string




Figure 3 again shows how the cells of the cube are linearized.



Sample input 



aa.a..a....................
.........a..a..aa..........



Sample output 



aababbadcggeffcddcgeegfedfc
aababbadceffgdcgdceefedfggc
...
aababbadcffegfcddcfeeggedgc

adcaccaacfddfebgeeffdggbgeb
...





Miguel Revilla
2001-06-15



