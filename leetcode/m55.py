from typing import List


class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0]
        target = 0
        while (target != (len(nums) - 1)) and (dp != []):
            tmp = [el for el in range(target+1, target + 1 + nums[target])]
            dp.extend(tmp)
            target = dp.pop()
        return dp != []

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if min(nums) != 0: # Если нет 0
            return True

        i_max_jump = 0
        for i in range(len(nums)-1):
            if nums[i] + i > i_max_jump:
                i_max_jump = nums[i] +  i
            print(i, nums[i], i_max_jump, i >= i_max_jump)
            if nums[i] == 0:
                if i >= i_max_jump:
                    return False
        return True



if __name__ == '__main__':
    s = Solution2()
    s2 = Solution()

    assert s.canJump([2,3,1,1,4]) == s2.canJump([2,3,1,1,4])
    assert s.canJump([3,2,1,0,4]) == s2.canJump([3,2,1,0,4])
    assert s.canJump([3, 2, 2, 0, 4]) == s2.canJump([3, 2, 2, 0, 4])
    assert s.canJump([2, 3, 1, 1, 0]) == s2.canJump([2, 3, 1, 1, 0])
    assert s.canJump([1,2,3]) == s2.canJump([1,2,3])