

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app45.us.archive.org';archive_analytics.values.server_ms=265;

__wbhack.init('https://web.archive.org/web');




Transaction Processing







 Transaction Processing 

You have been called upon to write a program which performs one of 
the initial steps in posting transactions to a general ledger. The 
central principle of double-entry bookkeeping is that the sum of all 
debits must equal the sum of all credits. This is true for each 
transaction. For the purposes of your program, positive numbers 
represent debits and negative numbers represent credits. That is, 
2.00 is a two dollar debit, and -2.00 is a two dollar credit. The 
purpose of your program is to check that each transaction balances, 
and to report it if it doesn't.

Input

Input data to your program will come in two sections. The first 
section is a list of up to 100 accounts in the general ledger. It consists 
of lines in the format:

nnnxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

where nnn is a three-digit account number and 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx is a 1-30 character account name 
string. This section is terminated by a record starting with 000, 
which is not used as an account number.


The second section of the input data consists of 15-character records,
one per line in the format

sssnnnxxxxxxxxx

where sss is a three-digit sequence number, nnn is a three-digit 
account number, and xxxxxxxxx is a nine-digit amount in dollars and 
cents (without the decimal point). Each of these records is one entry 
of a transaction. A transaction consists of between two and ten 
entries with identical sequence numbers. Each transaction will be 
contiguous within the input data. This section of input data is 
terminated by a record which has a sequence number of 000.

Output

Nothing is to be printed for transactions which balance. For 
transactions which do not balance, an exception report is to be 
printed in the form:

*** Transaction sss is out of balance ***
nnn xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx vvvvvvv.vv
nnn xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx vvvvvvv.vv
.
.
.
999 Out of Balance                 vvvvvvv.vv

where nnn is an account number, xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
is the corresponding account name, and vvvvvvv.vv is the amount. 
Print a space between the above fields. The entries should be listed 
in the order that they were received in the input. The last entry in 
the report is one you will create to make the transaction balance, 
using the special account number 999 (the suspense account). Print a 
blank line after each exception report.

Sample input

111Cash 
121Accounts Receivable
211Accounts Payable
241Sales Tax Payable 
401Sales
555Office Supplies
000No such account
100111    11795
100121   -11795
101121      105
101241       -7 
101401     -100
102211   -70000
102555    40000
103111   -40000 
103555    40000
000000        0

Sample output

*** Transaction 101 is out of balance ***
121 Accounts Receivable                  1.05
241 Sales Tax Payable                   -0.07
401 Sales                               -1.00
999 Out of Balance                       0.02

*** Transaction 102 is out of balance ***
211 Accounts Payable                  -700.00
555 Office Supplies                    400.00
999 Out of Balance                     300.00



