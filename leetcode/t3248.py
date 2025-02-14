from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        position = 0
        moves = {'RIGHT': 1, 'LEFT': -1, 'UP': -n, 'DOWN': n}
        for command in commands:
            position += moves[command]
        return position

def test_program():
    s = Solution()


    assert s.finalPositionOfSnake(2,['RIGHT', 'DOWN']) == 3
    assert s.finalPositionOfSnake(3,["DOWN","RIGHT","UP"]) == 1