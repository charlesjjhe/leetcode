from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []
        if len(nums) == 0:
            return ret
        s = nums[0]
        e = nums[0]
        i = 1
        l = len(nums)
        while i < len(nums):
            if nums[i] - e > 1:
                if e == s:
                    ret.append(f'{e}')
                else:
                    ret.append(f'{s}->{e}')
                s = nums[i]
                e = nums[i]
            elif nums[i] - e == 1 or nums[i] - e == 0:
                e = nums[i]
            i += 1
        if e == s:
            ret.append(f'{e}')
        else:
            ret.append(f'{s}->{e}')
        return ret




