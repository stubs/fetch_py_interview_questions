#!/usr/bin/env python
from itertools import permutations


def make_permutations(in_list, combo_len=3):
    """Produce unique permutations of input items in list.  Return list of permutations."""
    return list(permutations(in_list, combo_len))


def wrangle_bin_states(in_string):
    """Convert variable length string into a list of integers. Return list."""
    clean_string_list = in_string.split()
    for item in clean_string_list:
        if str.isalpha(item):
            print "{} cannot be converted to list of integers.".format(in_string)
            return False
    int_list = [int(x) for x in clean_string_list]
    return int_list


def list_to_bin_dict(in_list):
    """Read in string from data file, separate string contents into dict of lists with different colored bottles in each
    bin."""
    if len(in_list) == 9:
        bin_dict = {}
        bin_dict["B"] = in_list[0:3]
        bin_dict["G"] = in_list[3:6]
        bin_dict["C"] = in_list[6:]
        return bin_dict
    else:
        print "{} has a length less than 9.".format(in_list)
        return False


def calc_bottle_moves(in_list, bin_position):
    """Given list of len(n) and index bin_position, sum other n-1 list items to calc total bottle moves."""
    if bin_position == 0:
        bottle_moves = sum(in_list[1:])
    elif bin_position == 1:
        bottle_moves = in_list[0] + in_list[2]
    elif bin_position == 2:
        bottle_moves = sum(in_list[0:2])
    return bottle_moves
