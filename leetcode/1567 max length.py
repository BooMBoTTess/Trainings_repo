"""
Произведение положительно, когда количество отрицательный чисел четное
"""
from typing import List


class Solution2:
    def _is_prod_positive(self, arr : List[int]):
        count_negative = 0
        for el in arr:
            if el < 0:
                count_negative += 1
        if count_negative % 2 == 0 :
            return True
        return False

    def slice_negative(self, arr: List[int]):
        left_negative, right_negative = 0,0
        flag = True
        for i in range(0, len(arr)):
            if arr[i] < 0:
                if flag:
                    left_negative = i
                    flag = False
                right_negative = i

        return arr[left_negative+1: len(arr)], arr[0: right_negative]

    def all_elements_zero(self, arr: List[int]):
        for el in arr:
            if el != 0:
                return False
        return True

    def getMaxLen(self, nums: List[int]) -> int:
        if self.all_elements_zero(nums):
            return 0
        # Обрезка по 0
        prev_zero = 0
        now_zero = 0
        slices = []
        flag = False
        print('\n__________', nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                now_zero = i
                if flag:
                    slices.append(nums[prev_zero+1:now_zero])
                else:
                    slices.append(nums[prev_zero:now_zero])
                prev_zero = now_zero
                flag = True
        if flag:
            slices.append(nums[prev_zero+1:len(nums)])
        else:
            slices.append(nums[prev_zero:len(nums)])
        print(slices)

        # Обрезка по < 0
        positive_lengths = []
        for el in slices:
            if self._is_prod_positive(el):
                positive_lengths.append(len(el))
            else:
                left, right = self.slice_negative(el)
                print(left, right)
                positive_lengths.append(len(left))
                positive_lengths.append(len(right))

        return max(positive_lengths)


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        longestSub = 0
        seenNeg = 0
        seenPos = 0

        for i in nums:
            if i > 0:
                seenPos += 1
                seenNeg += 1 if seenNeg else 0
            elif i < 0:
                op = seenPos
                seenPos = 1 + seenNeg if seenNeg else 0
                seenNeg = 1 + op

            else:
                seenPos = seenNeg = 0

            longestSub = max(longestSub, seenPos)

        return longestSub

if __name__ == '__main__':
    s = Solution()
    print(s.slice_negative([-7, -10, -7, 21, 20, -12, -34, 26, 2]))

    assert s.slice_negative([-7, -10, -7, 21, 20, -12, -34, 26, 2]) == ([-10, -7, 21, 20, -12, -34, 26, 2], [-7, -10, -7, 21, 20, -12])
    assert s.getMaxLen([1,-2,-3,4]) == 4
    assert s.getMaxLen([-1, -2, -3, 0,1]) == 2
    assert s.getMaxLen([6,2,10,1,-2,8]) == 4
    assert s.slice_negative([1, 2, 3, 5, -6, 4, 0, 10]) == ([4,0,10],[1,2,3,5])
    assert s.getMaxLen([1,2,3,5,-6,4,0,10]) == 4
    assert s.getMaxLen([5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]) == 8


