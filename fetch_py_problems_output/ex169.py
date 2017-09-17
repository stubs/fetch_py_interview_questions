

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app46.us.archive.org';archive_analytics.values.server_ms=739;

__wbhack.init('https://web.archive.org/web');




Xenosemantics







 Xenosemantics 

Contact with extra-terrestrial intelligence has been made at last!! A
stream of messages has been discovered, apparently emanating from
Procyon IV. After intensive study by the world's best
xenosemanticists, the following definite conclusions on the format of
the messages have been reached. The messages are streams of bits
divided into groups of 8. Somewhat coincidentally the meaningful parts
of the message map onto the lower case alphabet, although other
characters sometimes intervene. Letters are organised into words
separated by spacer letters. The spacer letter varies within a
message, but a word which is delimited by a particular spacer pair
does not contain that spacer letter within it. In addition the message
is conceptually bounded by a pair of `joker' letters or `wild spacers'
that can match any letter. For example, a message segment 
xwrxwtx contains 3 words--wr, wt, and rx; wrxwt is
not a word in this segment of the message. If this segment appeared at
the start of a message then xw and xwrxw could also be
words. The words wr and rx overlap, while wt does
not overlap any words in this message segment. While a word contains
the same letters each time it appears in one message, the order of the
letters may vary in different occurrences of the same word. Each
message contains many words which are not ``true'' words in that they
carry no meaning (like err.., umm.., etc in English). Every true word
in the message contains at least two and no more than 250 letters,
overlaps with another true word, and is repeated somewhere in the
message (possibly with the letters in a different order). In the
example above, wr and rx would both be true words if 
wr or rw, and rx or xr, occurred as words elsewhere
in the message. The word wt would be a true word if wt or
tw occurred elsewhere in the message, overlapping another true
word.


Write a program that will read in messages and print out a list of the
different true words contained in each message (using the spelling
which occurs first), in the order the words first appear in the
message. If the first appearances of two words overlap, then the word
that finishes first precedes the other. Remember that both the start
and the end of the message count as spacer letters. Your program must
be able to process messages of up to 1000 letters.

Input

Input will consist of one or more messages. Each message will consist
of one or more lines. Each line will be no more than 60 characters
long and will contain a mixture of lower case letters and other
characters. If the last character of a line is a dash (-) then the
message continues on the next line. All characters other than lower
case `a' to `z' form no part of the message. The file will be
terminated by a line consisting of a single #.

Output

Output will consist of the true words for each message, in the correct
order as specified above, one word per line. Terminate the list for
each message by a line consisting of a single *.

Sample input

dyj@ttdi%sdort^jdyt*rFnn  trlnsvkGHoalexotrjxzasvs-
ozgpsi<>:pkelaovo,.;'slnxt'][-prsjlntrjo
aaaaaaa
#

Sample output

dyj
ortj
lnsvkoalexot
*
*



