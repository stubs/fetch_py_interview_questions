

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app45.us.archive.org';archive_analytics.values.server_ms=458;

__wbhack.init('https://web.archive.org/web');




The Errant Physicist







 The Errant Physicist 

The well-known physicist Alfred E Neuman is working on problems that 
involve multiplying polynomials of x and y.  For example, he may need to 
calculate

  

getting the answer

  

Unfortunately, such problems are so trivial that the great man's mind keeps 
drifting off the job, and he gets the wrong answers.  As a consequence, 
several nuclear warheads that he has designed have detonated prematurely, 
wiping out five major cities and a couple of rain forests.


You are to write a program to perform such multiplications and save the 
world.

Input

The file of input data will contain pairs of lines, with each line containing 
no more than 80 characters.  The final line of the input file contains a 
# as 
its first character.  Each input line contains a polynomial written without 
spaces and without any explicit exponentiation operator.  Exponents are 
positive non-zero unsigned integers.  Coefficients are also integers, but may 
be negative.  Both exponents and coefficients are less than or equal to 100 
in magnitude.  Each term contains at most one factor in x and one in y.

Output

Your program must multiply each pair of polynomials in the input, and print 
each product on a pair of lines, the first line containing all the exponents, 
suitably positioned with respect to the rest of the information, which is in 
the line below.


The following rules control the output format:

 Terms in the output line must be sorted in decreasing order of powers 
of x and, for a given power of x, in increasing order of powers of y.
 Like terms must be combined into a single term.  For example, 
40x2y3
- 38x2y3 is replaced by 2x2y3.
 Terms with a zero coefficient must not be displayed. Coefficients of 1 are omitted, except for the case of a constant term 
of 1.
 Exponents of 1 are omitted.
 Factors of x0  and y0 are omitted.
 Binary pluses and minuses (that is the pluses and minuses connecting 
terms in the output) have a single blank column both before and after.
 If the coefficient of the first term is negative, it is preceded by a 
unary minus in the first column, with no intervening blank column.  
Otherwise, the coefficient itself begins in the first output column.
 The output can be assumed to fit into a single line of at most 80 
characters in length.
 There should be no blank lines printed between each pair of output 
lines.
 The pair of lines that contain a product should be the same
length--trailing blanks should appear after the last non-blank character
of the shorter line to achieve this.

Sample Input


-yx8+9x3-1+y
x5y+1+x3
1
1
#


Sample Output


  13 2    11      8      6    5     5 2     3    3
-x  y  - x  y + 8x y + 9x  - x y + x y  + 8x  + x y - 1 + y 

1




