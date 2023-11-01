import task_1 as t
import pytest
import random


def test_partition():
    assert t.partition(3, [1,9,4,2,3],3) == (2, 3)
    assert t.partition(0, [], 0) == (0,0)
    assert t.partition(1,[0], 0) == (0, 1)


pytest.main()
