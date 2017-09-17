

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app36.us.archive.org';archive_analytics.values.server_ms=219;

__wbhack.init('https://web.archive.org/web');




Gondwanaland Telecom







 Gondwanaland Telecom 

Gondwanaland Telecom makes charges for calls according to distance and
time of day. The basis of the charging is contained in the following
schedule, where the charging step is related to the distance:

  

All charges are in dollars per minute of the call. Calls which
straddle a rate boundary are charged according to the time spent in
each section. Thus a call starting at 5:58 pm and terminating at 6:04
pm will be charged for 2 minutes at the day rate and for 4 minutes at
the evening rate. Calls less than a minute are not recorded and no
call may last more than 24 hours.


Write a program that reads call details and calculates the
corresponding charges.

Input and Output

Input lines will consist of the charging step (upper case letter
'A'..'E'), the number called (a string of 7 digits and a hyphen in the
approved format) and the start and end times of the call, all
separated by exactly one blank. Times are recorded as hours and
minutes in the 24 hour clock, separated by one blank and with two
digits for each number. Input will be terminated by a line consisting
of a single #.


Output will consist of the called number, the time in minutes the call
spent in each of the charge categories, the charging step and the
total cost in the format shown below.

Sample input

A 183-5724 17 58 18 04
#

Sample output


  



