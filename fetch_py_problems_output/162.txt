

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app17.us.archive.org';archive_analytics.values.server_ms=232;

__wbhack.init('https://web.archive.org/web');




Beggar My Neighbour







 Beggar My Neighbour 

``Beggar My Neighbour'' (sometimes known as ``Strip
Jack Naked'') is a traditional card game, designed to help teach
beginners something about cards and their values. A standard deck is
shuffled and dealt face down to the two players, the first card to the
non-dealer, the second to the dealer, and so on until each player has
26 cards. The dealer receives the last card. The non-dealer starts the
game by playing the top card of her deck (the second last card dealt)
face up on the table. The dealer then covers it by playing her top
card face up. Play continues in this fashion until a
``face'' card (Ace, King, Queen or Jack) is played. The next
player must then ``cover'' that card, by playing one
card for a Jack, two for a Queen, three for a King and four for an
Ace. If a face card is played at any stage during this sequence, play
switches and the other player must cover that card. When this sequence
has ended, the player who exposed the last face card takes the entire
heap, placing it face down under her existing deck. She then starts
the next round by playing one card face up as before, and play
continues until one player cannot play when called upon to do so,
because they have no more cards.


Write a program that will simulate playing this game. Remember that a
standard deck (or pack) of cards contains 52 cards. These are divided
into 4 suits--Spades (  ), Hearts (  ),
Diamonds (  ) and Clubs (  ). Within each
suit there are 13 cards--Ace (A), 2-9, Ten (T), Jack
(J), Queen (Q) and King (K).

Input

Input will consist of a
series of decks of cards. Each deck will give the cards in order as
they would be dealt (that is in the example deck below, the non-dealer
would start the game by playing the H2). Decks will occupy 4 lines
with 13 cards on each. The designation of each card will be the suit
(S, H, D, C) followed by the rank (A, 2-9, T, J, Q, K). There
will be exactly one space between cards. The file will be terminated
by a line consisting of a single #.

Output

Output will consist of a series of lines, one for each deck in the
input. Each line will consist of the number of the winning player (1
is the dealer, 2 is the first to play) and the number of cards in the
winner's hand (ignoring any on the stack), right justified in a field
of width 3.

Sample input

HA H3 H4 CA SK S5 C5 S6 C4 D5 H7 HJ HQ
D4 D7 SJ DT H6 S9 CT HK C8 C9 D6 CJ C6
S8 D8 C2 S2 S3 C7 H5 DJ S4 DQ DK D9 D3
H9 DA SA CK CQ C3 HT SQ H8 S7 ST H2 D2
#

Sample output

1 44



