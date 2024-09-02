from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        nums.sort()
        i = 0
        if l % 2 == 0:
            i = int(l/2)
            print(i)
        else:
            i = int((l-1) / 2)
        return nums[i]

if __name__ == "__main__":
    s = Solution()
    nums = [-1,1,1,1,2,1]
    print(s.majorityElement(nums))

    nums = [3,3,4]
    s.majorityElement(nums)

