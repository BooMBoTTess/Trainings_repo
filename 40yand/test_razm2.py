import razm2
import time
import pytest
from math import gcd
from fractions import Fraction


def test_solution():
    assert razm2.Solution('1 1 2 3') == '3 5'
    assert razm2.Solution('1 2 1 2') == '1 1'

def test_gcp():
    for i in range(1, 100):
        for j in range(1, 100):
            assert razm2.mygcd(i,j) == gcd(i, j)






pytest.main()