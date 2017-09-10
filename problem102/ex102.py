#!/usr/bin/env python
# coding=utf-8
"""Ecological Bin Packing 
Background

Bin packing, or the placement of objects of certain weights into
different bins subject to certain constraints, is an historically
interesting problem.  Some bin packing problems are NP-complete but are
amenable to dynamic programming solutions or to approximately optimal
heuristic solutions.

In this problem you will be solving a bin packing problem that deals
with recycling glass.

The Problem

Recycling glass requires that the glass be separated by color into one
of three categories: brown glass, green glass, and clear glass.  In this
problem you will be given three recycling bins, each containing a
specified number of brown, green and clear bottles.  In order to be
recycled, the bottles will need to be moved so that each bin contains
bottles of only one color.

The problem is to minimize the number of bottles that are moved.  You
may assume that the only problem is to minimize the number of movements
between boxes.

For the purposes of this problem, each bin has infinite
capacity and the only constraint is moving the bottles so that each
bin contains bottles of a single color. The total number of bottles will never exceed 2^31.

The Input

The input consists of a series of lines with each line containing 9
integers.  The first three integers on a line represent the number of
brown, green, and clear bottles (respectively) in bin number 1, the
second three represent the number of brown, green and clear bottles
(respectively) in bin number 2, and the last three integers
represent the number of brown, green, and clear bottles
(respectively)
in bin number 3.  For example, the line
10 15 20 30 12 8 15 8 31

indicates that there are 20 clear bottles in bin 1, 12 green bottles in
bin 2, and 15 brown bottles in bin 3.

Integers on a line will be separated by one or more spaces.  Your
program should process all lines in the input file.

The Output

For each line of input there will be one line of output indicating what color
bottles go in what bin to minimize the number of bottle movements.
You should also print the minimum number of bottle movements.

The output should consist of a string of the
three upper case characters 'G', 'B',
'C' (representing the colors green, brown, and clear) representing the
color associated with each bin.

The first character of the string
represents
the color associated with the first bin, the second character of the
string represents the color associated with the second bin, and the
third character represents the color associated with the third bin.

The integer indicating the minimum number of bottle movements
should follow the string.

If more than one order of brown, green, and clear bins
yields the minimum number of movements
then the alphabetically first string representing a minimal
configuration should be printed.

Sample Input
1 2 3 4 5 6 7 8 9
5 10 5 20 10 5 10 20 10

Sample Output
BCG 30
CBG 50
"""
import sys
import ex102_funcs as ex102


bin_states = sys.argv[1]
bins = ["B", "G", "C"]
bin_permutations = ex102.make_permutations(bins)


with open(bin_states, "rU") as bin_data:
    for row in bin_data:
        min_bottle_moves = 0  # instantiate
        row = row.replace("\n", "")
        row = ex102.wrangle_bin_states(row)
        row_dict = ex102.list_to_bin_dict(row)
        for combo in bin_permutations:
            bin_values = [ex102.calc_bottle_moves(row_dict[val], it) for it, val in enumerate(combo)]
            move_dict = dict(zip(combo, bin_values))
            total_bottle_moves = sum(move_dict.values())
            if min_bottle_moves == 0:
                min_bottle_moves = total_bottle_moves
                ideal_moves = ("".join(combo), min_bottle_moves)
            else:
                if total_bottle_moves < min_bottle_moves:
                    min_bottle_moves = total_bottle_moves
                    ideal_moves = ("".join(combo), min_bottle_moves)
        print ideal_moves[0], ideal_moves[1]
