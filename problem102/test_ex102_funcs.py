#!usr/bin/env python
import ex102_funcs as ex102


def test_make_permutations_3_in_items():
    # ex. ["a", "b", "c"] => ["abc", "acb", "bac", "bca", "cab", "cba"]
    assert len(ex102.make_permutations(["a", "b", "c"])) == 6


def test_wrangle_bin_states_variable_whitespace():
    assert ex102.wrangle_bin_states("1   22    39  4") == [1, 22, 39, 4]


def test_wrangle_bin_states_err_w_text():
    assert ex102.wrangle_bin_states("Hello World!") is False


def test_list_to_bin_dict_len_9_list():
    in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    out_dict = {"B": [1, 2, 3], "G": [4, 5, 6], "C": [7, 8, 9]}
    assert ex102.list_to_bin_dict(in_list) == out_dict


def test_list_to_bin_dict_less_than_9_list():
    in_list = [1, 2, 3, 4]
    assert ex102.list_to_bin_dict(in_list) is False


def test_calc_bottle_moves():
    in_list = [1, 2, 3]
    assert ex102.calc_bottle_moves(in_list, 0) == 5
    assert ex102.calc_bottle_moves(in_list, 1) == 4
    assert ex102.calc_bottle_moves(in_list, 2) == 3