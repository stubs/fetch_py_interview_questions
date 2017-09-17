

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app22.us.archive.org';archive_analytics.values.server_ms=946;

__wbhack.init('https://web.archive.org/web');




Following Orders







 Following Orders 

Background

Order is an important concept in mathematics and in computer science.
For example, Zorn's Lemma states:  ``a partially ordered set in which
every chain has an upper bound contains a maximal element.''
Order is also important in reasoning about the fix-point semantics of
programs.


This problem involves neither Zorn's Lemma nor fix-point semantics, but
does involve order.

The Problem

Given a list of variable constraints of the form
x < y, you are to write a program that prints all
orderings of the variables that are consistent with the constraints.


For example, given the constraints x < y  and x < z there
are two orderings of the variables x, y, and z that are consistent with these
constraints:  x y z and x z y.

The Input

The input consists of a sequence of constraint specifications.  A
specification consists of two lines: a list of variables on one line
followed by a list of constraints on the next line.  A constraint is
given by a pair of variables, 
where x y indicates that x < y.


All variables are single character, lower-case letters.  There will be
at least two variables, and no more than 20 variables in a specification.
There will be at least one constraint, and no more than 50 constraints
in a specification.  There will be at least one, and no more than 300
orderings consistent with the contraints in a specification.


Input is terminated by end-of-file.

The Output

For each constraint specification, all orderings consistent with
the constraints should be printed.   
Orderings are printed in lexicographical (alphabetical) order, one per
line.


Output for different constraint specifications is separated by a blank line.

Sample Input

a b f g
a b b f
v w x y z
v y x v z v w v

Sample Output

abfg
abgf
agbf
gabf

wxzvy
wzxvy
xwzvy
xzwvy
zwxvy
zxwvy



