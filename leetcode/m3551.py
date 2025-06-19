from typing import List

import pytest


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        cp_nums = nums.copy()
        nums_el_sum = [sum(list(map(int, str(el)))) for el in nums]
        counter_changed_values = 0

        flag = True



        while flag: # Сортировка обоих массивов
            flag = False
            for i in range(len(nums_el_sum)-1):
                if nums_el_sum[i] > nums_el_sum[i + 1]:
                    tmp = nums_el_sum[i]
                    nums_el_sum[i] = nums_el_sum[i + 1]
                    nums_el_sum[i + 1] = tmp

                    tmp = cp_nums[i]
                    cp_nums[i] = cp_nums[i + 1]
                    cp_nums[i + 1] = tmp

                    flag = True

                if nums_el_sum[i] == nums_el_sum[i + 1]:
                    if cp_nums[i] > cp_nums[i + 1]:
                        tmp = nums_el_sum[i]
                        nums_el_sum[i] = nums_el_sum[i + 1]
                        nums_el_sum[i + 1] = tmp

                        tmp = cp_nums[i]
                        cp_nums[i] = cp_nums[i + 1]
                        cp_nums[i + 1] = tmp

                        flag = True

        # Поиск изменений

        for i in range(len(nums)):
            if nums[i] != cp_nums[i]:
                counter_changed_values += 1

        print('\n',cp_nums)
        if counter_changed_values % 2 != 0:
            return counter_changed_values // 2 + 1
        return counter_changed_values // 2

test_data = [
[[37,100], 1],
[[22,14,33,7], 0],
[[18,43,34,16], 2],
[[268835996,65052660,415128775], 2],
[[277993448,416038674,616955867,539372283], 3]
]


@pytest.mark.parametrize('test_input, test_output', test_data)
def test_solution(test_input, test_output):
    s = Solution()
    assert s.minSwaps(test_input) == test_output

