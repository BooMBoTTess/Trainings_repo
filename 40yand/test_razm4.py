import razm4 as t
import pytest



def test_solution():
    assert t.Solution([1, 3, 4]) == [5, 3, 4]
    assert t.Solution([3,7,8,10,15]) == [28,16,15,17,32]

def test_max_time():
    assert t.Solution([1000 for i in range(10000)]) == [0 for i in range(10000)]


pytest.main()