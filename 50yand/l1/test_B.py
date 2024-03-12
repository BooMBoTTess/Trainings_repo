import B_dev as t
import pytest
import random


def test_partition():
    # Перекрещены
    assert t.Solution((0, 0), (0, 0), 1) == 1
    assert t.Solution((0, 2), (0, 3), 2) == 6
    assert t.Solution((0, 2), (0, 3), 1) == 5

pytest.main()
