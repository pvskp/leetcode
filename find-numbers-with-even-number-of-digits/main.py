import math
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([x for x in nums if (math.floor(math.log10(x)) + 1) % 2 == 0])


s = Solution()
print(s.findNumbers([555, 901, 482, 1771]))
