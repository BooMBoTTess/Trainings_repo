from typing import List


class Solution:
    def numIdenticalPairs(self, arr: List[int]):
        pairs_count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    pairs_count += 1
        return pairs_count




if __name__ == '__main__':
    s = Solution()
    print(s.numIdenticalPairs([1,2,3,1,1,3]))