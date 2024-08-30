from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = set()
        d = []
        for i in nums:
            if i not in a:
                d.append(i)
                a.add(i)
        for i in range(0, len(a)):
            nums[i] = d[i]
        return len(a)



