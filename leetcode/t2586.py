from typing import List

vowels = ['a', 'e', 'i', 'o', 'u']
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        number_vowel = 0
        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][len(words[i]) - 1] in vowels:

                number_vowel += 1
        return number_vowel


def test_program():
    s = Solution()
    assert s.vowelStrings(["are","amy","u"], 0, 2) == 2
    assert s.vowelStrings(["hey","aeo","mu","ooo","artro"], 1, 4) == 3