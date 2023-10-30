import razm2
import time
import pytest

def test_solution():
    assert razm2.Solution('1 1 2 3') == '3 5'
    assert razm2.Solution('1 2 1 2') == '1 1'
    assert razm2.Solution('1 1 2 3') == '3 5'


pytest.main()