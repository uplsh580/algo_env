# https://leetcode.com/problems/jump-game-ii/
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_pos = [i + j for i, j in enumerate(nums)]
        print(max_pos)
        # return answer


if __name__ == '__main__':
    nums = [2, 3, 0, 1, 4]
    s = Solution()
    s.jump(nums)
