

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app42.us.archive.org';archive_analytics.values.server_ms=249;

__wbhack.init('https://web.archive.org/web');




Permalex







 Permalex 

Given a string of characters, we can permute the individual characters
to make new strings. If we can impose an ordering on the characters
(say alphabetic sequence), then the strings themselves can be ordered
and any given permutation can be given a unique number designating its
position in that ordering. For example the string `acab' gives rise to
the following 12 distinct permutations:

  

Thus the string `acab' can be characterised in this sequence as 5.


Write a program that will read in a string and determine its position
in the ordered sequence of permutations of its constituent characters.
Note that numbers of permutations can get very large; however we
guarantee that no string will be given whose position is more than
  .

Input and Output

Input will consist of a series of lines, each
line containing one string. Each string will consist of up to 30 lower
case letters, not necessarily distinct. The file will be terminated by
a line consisting of a single #.


Output will consist of a series of lines, one for each line of the
input. Each line will consist of the position of the string in its
sequence, right justified in a field of width 10.

Sample input

bacaa
abc
cba
#

Sample output


        15
         1
         6




