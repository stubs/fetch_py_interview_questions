

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app45.us.archive.org';archive_analytics.values.server_ms=551;

__wbhack.init('https://web.archive.org/web');




Bonus Bonds







 Bonus Bonds 

The government of Impecunia does not levy any taxes, instead it raises
money by the (sometimes forced) sale of Bonus Bonds. Originally the
Bonds were numbered using a 7 digit number prefixed by a one digit
code in the range 1 to 9 representing the region of Impecunia in which
the bond was sold. However the scheme has proved so popular that the
numbering scheme has been extended by a further two digits. To retain
compatibility with the previous scheme, the 8th digit from the right
(the third from the left) still designates the region of sale. At the
same time, a `central' region was created and has been given the
designation 0. For security reasons no bond may be numbered with a
number consisting entirely of zeroes, thus, although the original
bonds all started from zero (since the region code was non-zero), the
bonds from the central region start from 0000000001.


Each month, the winning numbers are drawn for each region
independently. The equipment generates a stream of single digits and
it would appear to be simple enough to collect these together in
groups of ten and compare the results with the list of Bond-holders.
However, the equipment is a little antiquated and is liable to various
breakdowns, thus it is desirable to only generate numbers that lie
within the allocated range and with the same distributions of digits
at each position as would be found by examining all the bonds sold for
that region. Thus if we wish to draw N numbers for a given region, the
equipment is set to generate 10 streams of N digits, one for each
position. The first winning number is then made up by taking the first
digit from each stream, the second winning number is composed of the
second digit in each stream, and so on. For each stream, the equipment
is adjusted so that the distribution of digits it generates closely
matches the actual distributions of digits in that position on the
allocated Bonds. The state auditors generate a table of these
distributions so that the two may be compared.


Write a program that will generate the table for the state auditors
for any given draw. For each region, the program will read the serial
number of the next bond to be sold in that region so that it can
calculate the distributions. Since the output is voluminous, your
program will only need to print the digit distribution for a
particular digit position.

Input

Input will consist of a series of lines, each line consisting of a ten
digit number representing the next bond number to be sold in a
particular region and an integer in the range 1 to 10 representing the
desired character position. It is possible that some regions will
appear more than once in the input stream, and that others will not
appear at all. The file will be terminated by a line consisting of
0000000000 0.

Output

Output will consist of a series of tables, one for each line of the
input. Each table will consist of ten rows, one for each digit in the
range 0 to 9. Each row will consist of a single number giving the
numbers of times that digit appears in the sequence numbers at the
desired position. Each number will be right justified in a field of
width 11. Separate tables by one blank line.

Sample input

4810000000 1
0000000000 0

Sample output

  100000000
  100000000
  100000000
  100000000
   80000000
          0
          0
          0
          0
          0



