

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app15.us.archive.org';archive_analytics.values.server_ms=321;

__wbhack.init('https://web.archive.org/web');




Double Time







 Double Time 

In 45 BC a standard calendar was adopted by Julius Caesar--each
year would have 365 days, and every fourth year have an extra
day--the 29th of February. However this calendar was not quite accurate
enough to track the true solar year, and it became noticeable that the
onset of the seasons was shifting steadily through the year. In 1582
Pope Gregory XIII ruled that a new style calendar should take effect.
From then on, century years would only be leap years if they were
divisible by 400. Furthermore the current year needed an adjustment to
realign the calendar with the seasons. This new calendar, and the
correction required, were adopted immediately by Roman Catholic
countries, where the day following Thursday 4 October 1582 was Friday
15 October 1582. The British and Americans (among others) did not
follow suit until 1752, when Wednesday 2 September was followed by
Thursday 14 September. (Russia did not change until 1918, and Greece
waited until 1923.) Thus there was a long period of time when history
was recorded in two different styles.


Write a program that will read in a date, determine which style it is
in, and then convert it to the other style.

Input

Input will consist of a
series of lines, each line containing a day and date (such as Friday 25
December 1992). Dates will be in the range 1 January 1600 to 31
December 2099, although converted dates may lie outside this range.
Note that all names of days and months will be in the style shown,
that is the first letter will be capitalised with the rest lower case.
The file will be terminated by a line containing a single `#'.

Output

Output will consist of a series of lines, one for each line of the
input. Each line will consist of a date in the other style. Use the
format and spacing shown in the example and described above. Note that
there must be exactly one space between each pair of fields. To
distinguish between the styles, dates in the old style must have an
asterisk (`*') immediately after the day of the month (with no
intervening space). Note that this will not apply to the input.

Sample input

Saturday 29 August 1992
Saturday 16 August 1992
Wednesday 19 December 1991
Monday 1 January 1900
#

Sample output

Saturday 16* August 1992
Saturday 29 August 1992
Wednesday 1 January 1992
Monday 20* December 1899



