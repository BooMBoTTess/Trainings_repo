import razm3 as t
import pytest



def test_solution():
    assert t.Solution('dsa', 'dsa') == True
    assert t.Solution('abc', 'efg') == False
    assert t.Solution('dsa', 'dsasdf') == False
    assert t.Solution('dsasdf', 'dsa') == False
    assert t.Solution('aaaa', 'aa') == False
    assert t.Solution('aboba', 'bobaa') == True
    assert t.Solution('dusty', 'study') == True
    assert t.Solution('rat', 'bat') == False


pytest.main()