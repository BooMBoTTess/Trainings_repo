class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 1
        while x < n:
            x = x * 4
        if x == n:
            return True
        return False


def test_program():
    s = Solution()


    assert s.isPowerOfFour(16) == True
    assert s.isPowerOfFour(5) == False
    assert s.isPowerOfFour(1) == True