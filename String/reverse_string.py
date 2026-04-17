from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]

s = ["K", "u", "r", "t"]

Sol = Solution()

Sol.reverseString(s)
print(s)