import random
from typing import List

import pytest


def last_pow(left, right):
    repeatable = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [1, 3, 9, 7],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [1, 7, 9, 3],
        8: [8, 4, 2, 6],
        9: [9, 1],
    }
    left_last_num = left % 10
    right_last_num = right % 10
    if right == 0:
        if left == 0:
            return 0
        return 1

    if left_last_num == 1:
        return left_last_num

    if left_last_num in [0,5,6]:
        return left_last_num

    if left_last_num in [4, 9]:
        return repeatable[left_last_num][(right-1) % 2]

    if left_last_num in [3,7]:
        return repeatable[left_last_num][right % 4]

    if left_last_num in [2,8]:
        return repeatable[left_last_num][(right - 1) % 4]


def last_digit(lst):
    if lst == 1:
        return lst % 10
    if len(lst) == 0:
        return 1
    if len(lst) == 2:
        return lst[0] ** lst[1] % 10

    digit = lst[len(lst) - 1] % 10
    print(digit)
    for i in range((len(lst) - 2), -1, -1):
        digit = last_pow(lst[i], digit)
        print(i, lst[i] ** digit, lst[i], digit, lst)


    return digit


test_data = [
[[], 1],
[[0,0,0], 0],
[[4, 3, 6], 4],
[[7, 6, 21], 1],
[[12, 30, 21], 6],
[[937640, 767456, 981242], 0],
[[123232, 694022, 140249], 6]
]

@pytest.mark.parametrize('test_input, test_output', test_data)
def test_solution(test_input, test_output):

    assert last_digit(test_input) == test_output

test_data = [
[[13,1], 3],
[[12,4], 6],
[[17,11], 3],
[[14,21], 4],
[[29,7], 9],
]

@pytest.mark.parametrize('test_input, test_output', test_data)
def test_last_pow(test_input, test_output):
    assert last_pow(test_input[0], test_input[1]) == test_output


def test_random_last_pow():
    for i in range(50):
        left = random.randint(0, 30)
        right = random.randint(0, 30)
        res = (left ** right) % 10
        assert last_pow(left, right) == res

