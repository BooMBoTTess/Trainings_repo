from typing import List


class Solution:


    def jump(self, arr: List[int]):
        length = len(arr)
        min_jump_to_end = [9999 for i in range(length)]
        tmp_index = length-2
        min_jump_to_end[length - 1] = 0

        while(tmp_index != -1):
            min_jump_in_index = 9999
            for i in range(tmp_index+1, tmp_index + arr[tmp_index] + 1):
                if i < length:
                    if min_jump_to_end[i] < min_jump_in_index:
                        min_jump_in_index = min_jump_to_end[i] + 1
            min_jump_to_end[tmp_index] = min_jump_in_index
            tmp_index -= 1

        return min_jump_to_end[0]

#[2,3,1,1,4] -> 2

# 0