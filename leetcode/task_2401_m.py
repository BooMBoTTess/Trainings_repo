from typing import List


class Solution:


    def longestNiceSubarray(self, nums: List[int]) -> int:
        len_subarrays = [0]
        pos_len = 0
        prev_bit_sum = 0
        i = 0
        for i in range(1, len(nums)):
            if not (nums[i] & prev_bit_sum):
                prev_bit_sum += nums[i]
                len_subarrays[pos_len] += 1
            else:
                len_subarrays.append(1)
                prev_bit_sum = nums[i]
                pos_len += 1

        if max(len_subarrays) == 0:
            return 1
        return max(len_subarrays)

s = Solution()

nums1 = [84139415,693324769,614626365,497710833,615598711,264,65552,50331652,1,1048576,16384,544,270532608,151813349,221976871,678178917,845710321,751376227,331656525,739558112,267703680]
print(s.longestNiceSubarray(nums1))
assert s.longestNiceSubarray(nums1) == 8


nums1 = [45106826,547958667,823366125,332020148,611677524,510346561,555831456,436600904,12594192,127206768,540754485,201997978,473116514,233000361,538246458,729745279,343417143,892046691,376031730]
print(s.longestNiceSubarray(nums1))
assert s.longestNiceSubarray(nums1) == 3

nums1 = [744437702,379056602,145555074,392756761,560864007,934981918,113312475,1090,16384,33,217313281,117883195,978927664]
print(s.longestNiceSubarray(nums1))
assert s.longestNiceSubarray(nums1) == 3


nums1 = [1,3,8,48,10]
print(s.longestNiceSubarray(nums1))
assert s.longestNiceSubarray(nums1) == 3

