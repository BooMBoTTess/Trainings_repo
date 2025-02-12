from typing import List


class Solution:

    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        for i in range(1, len(pref)):
            arr.append(pref[i-1] ^ pref[i])
        return arr



s = Solution()
nums1 = [5,2,0,3,1]
assert s.findArray(nums1) == [5,7,2,3,2]
print(nums1)