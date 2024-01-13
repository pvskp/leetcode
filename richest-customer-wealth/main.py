from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        higher = 0
        for ac in accounts:
            s = sum(ac)
            if s > higher:
                higher = s

        return higher


s = Solution()
print(s.maximumWealth([[1, 5], [7, 3], [3, 5]]))
