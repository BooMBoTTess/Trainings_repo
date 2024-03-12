import B_dev as t
import B_dev as corr
import pytest
import random


def test_partition():
    # Перекрещены
    assert t.Solution((0, 0), (0, 0), 1) == 1
    assert t.Solution((0, 2), (0, 3), 1) == 5
    assert t.Solution((0, 2), (0, 3), 2) == 6
    assert t.Solution((2, 2), (1, 1), 2) == 0
    assert t.Solution((2, 2), (1, 1), 1) == 1
    assert t.Solution((1, 2), (2, 3), 1) == 2
    assert t.Solution((1, 1), (0, 1), 1) == 2
    assert t.Solution((4, 3), (0, 3), 2) == 2
    assert t.Solution((4, 5), (2, 4), 2) == 4

def test_random():
    for i in range(1000):
        match_prev = (random.randint(0,5), random.randint(0,5))
        match = (random.randint(0,5), random.randint(0,5))
        home = random.randint(0,2)
        assert t.Solution(match_prev, match, home) == corr.Solution(match_prev, match, home)
pytest.main()
