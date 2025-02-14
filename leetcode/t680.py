from typing import List


class Solution:
    def _check_valid(self, s: str) -> (int, int):
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return l,r
            l += 1
            r -= 1
        return 0, 0


    def validPalindrome(self, s: str) -> bool:
        l,r = self._check_valid(s)
        if (l,r) == (0,0): # Проверка валидна ли строка
            return True

        tmp = s[:l] + s[l + 1:] # Убрали левый символ
        if self._check_valid(tmp) == (0,0):
            return True

        tmp = s[:r] + s[r + 1:] # Убрали правый символ
        if self._check_valid(tmp) == (0, 0):
            return True

        return False


def test_program():
    s = Solution()
    assert s.validPalindrome('abcba') == True
    assert s.validPalindrome('aba') == True
    assert s.validPalindrome('abc') == False
    assert s.validPalindrome('abba') == True
    assert s.validPalindrome('aaabbb') == False
    assert s.validPalindrome('abbca') == True
    assert s.validPalindrome('abca') == True
    assert s.validPalindrome('aaabbb') == False
    assert s.validPalindrome('abbbb') == True
    assert s.validPalindrome('bbbba') == True
    assert s.validPalindrome('') == True
    assert s.validPalindrome('aa') == True
    assert s.validPalindrome('aabcccba') == True