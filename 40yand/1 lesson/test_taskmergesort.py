import taskmergesort as t
import pytest
import random


def test_merge():
    assert t.merge([2, 5], [1, 2, 9]) == [1, 2, 2, 5, 9]
    assert t.merge([2, 3, 5], [1, 2]) == [1, 2, 2, 3, 5]
    assert t.merge([2,3,5], [1, 2, 9]) == [1,2,2,3,5,9]
    assert t.merge([2, 3], [1, 2]) == [1, 2, 2, 3]

def test_random():
    for i in range(10):
        li = [random.randint(1,50) for i in range(random.randint(2,30))]
        rl = li
        random.shuffle(rl)
        t.Solution(rl) == li

pytest.main()
