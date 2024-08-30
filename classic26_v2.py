from typing import List
from collections import OrderedDict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_od = OrderedDict.fromkeys(nums)
        unique_list_ordered = list(unique_od.keys())
        for i in range(0, len(unique_list_ordered)):
            nums[i] = unique_list_ordered[i]
        return len(unique_list_ordered)



