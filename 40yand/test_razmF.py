import razmF as t
import pytest
import random

def test_solution():
    assert t.Solution(2, 1, [2]) == t.bad_solution(2, 1, [2])
    assert t.Solution(2, 3, [3, 0, 1]) == 8
    assert t.Solution(2, 6, [2, 0, 0, 0, 0, 1]) == t.bad_solution(2, 6, [2, 0, 0, 0, 0, 1])
    assert t.Solution(2, 6, [5,3,1,4,2]) == t.bad_solution(2, 6, [5,3,1,4,2])
    assert t.Solution(3, 6, [2, 0, 2, 0, 2]) == t.bad_solution(3, 6, [2, 0, 2, 0, 2])

def test_finalboxx():
    for i in range(1000):
        k = random.randint(1,100)
        n = random.randint(1,100)
        arr =[random.randint(1,1000) for i in range(random.randint(1,1000))]
    assert t.Solution(k,n,arr) == t.bad_solution(k,n,arr)


def test_max_time():
    #assert t.Solution(1, 10000, [10000 for i in range(10000)]) == 333333330003
    pass

pytest.main()
