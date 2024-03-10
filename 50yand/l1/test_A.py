import A_dev as t
import pytest
import random


def test_partition():
    assert t.Solution(0, 7, 12, 5) == 25
    assert t.Solution(1, 7, 12, 5) == 24
    assert t.Solution(-1, 7, 12, 5) == 26
    assert t.Solution(-1, 1, 1, 1) == 5
    assert t.Solution(12, 7, 0, 5) == 25
    assert t.Solution(-1, 1, 4, 4) == 11
    assert t.Solution(0,0,0,0) == 1
    assert t.Solution(1, 2, 12, 1) == 8
    assert t.Solution(0, 0, 15, 0) == 2
    assert t.Solution(3, 1, 3, 3) == 7




pytest.main()