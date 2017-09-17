

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app41.us.archive.org';archive_analytics.values.server_ms=184;

__wbhack.init('https://web.archive.org/web');




Car Trialling







 Car Trialling 

Car trialling requires the following of carefully worded instructions.
When setting a trial, the organiser places traps in the instructions
to catch out the unwary.


Write a program to determine whether an instruction obeys the
following rules, which are loosely based on real car trialling
instructions. BOLD-TEXT indicates text as it appears in the
instruction (case sensitive),    separates options of which
exactly one must be chosen, and .. expands, so A..D
is equivalent to A  B  C  D .

instruction = navigational      time-keeping      navigational AND time-keeping

navigational = directional      navigational AND THEN directional

directional = how direction      how direction where

how = GO  GO when    KEEP

direction = RIGHT  LEFT

when = FIRST   SECOND  THIRD

where = AT sign

sign = "signwords"

signwords = s-word      signwords s-word

s-word = letter      s-word letter

letter = A..Z  .

time-keeping = record      change

record = RECORD TIME

change = cas TO nnn KMH

cas = CHANGE AVERAGE SPEED  CAS

nnn = digit      nnn digit

digit = 0..9
Note that s-word and nnn are sequences of letters and digits
respectively, with no intervening spaces. There will be one or more
spaces between items except before a period (.), after the opening
speech marks or before the closing speech marks.

Input

Each input line will consist of not more than 75 characters. The input
will be terminated by a line consisting of a single #.

Output

The output will consist of a series of sequentially numbered lines,
either containing the valid instruction, or the text Trap! if the
line did not obey the rules. The line number will be right justified
in a field of 3 characters, followed by a full-stop, a single space,
and the instruction, with sequences of more than one space reduced to
single spaces.

Sample input

KEEP LEFT AND THEN GO RIGHT
CAS TO 20 KMH
GO FIRST       RIGHT AT "SMITH ST."  AND   CAS TO 20 KMH
GO 2nd RIGHT
GO LEFT AT "SMITH STREET AND RECORD TIME
KEEP RIGHT AND THEN RECORD TIME
#

Sample output

  1. KEEP LEFT AND THEN GO RIGHT
  2. CAS TO 20 KMH
  3. GO FIRST RIGHT AT "SMITH ST." AND CAS TO 20 KMH
  4. Trap!
  5. Trap!
  6. Trap!



