

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app16.us.archive.org';archive_analytics.values.server_ms=633;

__wbhack.init('https://web.archive.org/web');




Word Crosses







 Word Crosses 

A word cross is formed by printing a pair of words, the first
horizontally and the second vertically, so that they share a common
letter. A leading word cross is one where the common letter is
as near as possible to the beginning of the horizontal word, and, for
this letter, as close as possible to the beginning of the vertical
word. Thus DEFER and PREFECT would cross on the first 'E' in each
word, PREFECT and DEFER would cross on the 'R'. Double leading
  word crosses use two pairs of words arranged so that the two
horizontal words are on the same line and each pair forms a leading
word cross.


Write a program that will read in sets of four words and form them (if
possible) into double leading word crosses.

Input

Input will consist of a series of lines, each line containing four
words (two pairs). A word consists of 1 to 10 upper case letters, and
will be separated from its neighbours by at least one space. The file
will be terminated by a line consisting of a single #.

Output

Output will consist of a series of double leading word crosses as
defined above. Leave exactly three spaces between the horizontal
words. If it is not possible to form both crosses, write the message
`Unable to make two crosses'. Leave 1 blank line
between output sets.

Sample input

MATCHES CHEESECAKE PICNIC EXCUSES
PEANUT BANANA VACUUM  GREEDY
#

Sample output

 C
 H
 E
 E
 S
 E          E
 C          X
MATCHES   PICNIC
 K          U
 E          S
            E
            S

Unable to make two crosses



