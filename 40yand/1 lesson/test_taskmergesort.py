import razmG as t
import pytest
import random


def test_merge():
    assert t.Solution(4,4[[1,1,1,1],[1,1,1,1][1,1,1,1][1,1,1,1]])

def test_random():
    for i in range(10):
        li = [random.randint(1,50) for i in range(random.randint(2,30))]
        rl = li
        random.shuffle(rl)
        t.Solution(rl) == li

pytest.main()
