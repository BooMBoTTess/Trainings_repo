from typing import List

import math


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for target_index in range(len(nums)-1, 0, -1):
            for target_place in range(target_index - 1, 0, -1):
                print(target_index, target_place)
                if nums[target_place] > nums[target_place-1]:
                    tmp = nums.pop(target_index)
                    nums.insert(target_place, tmp)

def test_program():
    s = Solution()
    arr = [1,2,3]
    s.nextPermutation(arr)
    assert arr == [1,3,2]
    s.nextPermutation(arr)
    assert arr == [2, 1, 3]
    s.nextPermutation(arr)
    assert arr == [2, 3, 1]
    s.nextPermutation(arr)
    assert arr == [3, 1, 2]
    s.nextPermutation(arr)
    assert arr == [3, 2, 1]
    arr = [3,2,1]
    s.nextPermutation(arr)
    assert arr == [1,2,3]



    arr = [1, 1, 5]
    s.nextPermutation(arr)
    assert arr == [1, 5, 1]