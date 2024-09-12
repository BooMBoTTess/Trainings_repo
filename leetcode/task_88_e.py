from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        res = []
        del(nums1[m:])
        del(nums2[n:])
        nums3 = []

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        if i < m:
            nums3.extend(nums1[i:])
        else:
            nums3.extend(nums2[j:])
        nums1.clear()
        nums1.extend(nums3)


s = Solution()
nums1 = [4,0,0,0,0,0]
s.merge(nums1, 1, [1,2,3,5,6], 5)
print(nums1)