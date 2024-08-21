#Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find_depth(self, depths):
        left_num = depths[0]
        curr_num = 0
        next_num = 0
        depth = 1
        i = 0
        while i < len(depths)-1:
            i += 1
            if left_num > curr_num:
                next_num += depths[i]
                curr_num += 1
            elif left_num == curr_num:
                next_num += depths[i]
                left_num = next_num
                next_num = 0
                curr_num = 1
                depth += 1

        return depth

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        depths = []
        points = [root]
        answers = []
        while points != []:
            tmp = points.pop()
            d = 0
            if tmp.left != None:
                points.append(tmp.left)
                d += 1
            if tmp.right != None:
                points.append(tmp.right)
                d += 1
            depths.append(d)

        return self.find_depth(depths)


if __name__ == '__main__':
    A = Solution()
    A.find_depth([1,1,1,1,0])
    root = [3, 9, 20, None, None, 15, 7]
