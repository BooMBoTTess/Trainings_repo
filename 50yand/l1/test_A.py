import A_dev as t
import pytest
import random


def test_partition():
    assert t.Solution(0, 7, 12, 5) == 25
    assert t.Solution(1, 7, 12, 5) == 24
    assert t.Solution(-1, 7, 12, 5) == 26
    assert t.Solution(-1, 1, 1, 1) == 5
    assert t.Solution(12, 7, 0, 5) == 25


pytest.main()
