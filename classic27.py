from typing import List

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        last_index = len(nums)
        if last_index == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        if last_index == 2:
            ret = 0
            if nums[0] != val:
                ret += 1
            if nums[1] != val:
                ret += 1
            if ret == 0 or ret == 2:
                return ret
            if nums[0] == val:
                nums[0], nums[1] = nums[1], nums[0]
            return ret
        pop_index = len(nums) - 1
        for i in range(0, last_index):
            for ii in range(0, pop_index):
                if nums[ii] == val:
                    nums[ii], nums[ii+1] = nums[ii+1], nums[ii]
                    pop_index -= 1
            pop_index -= 1
        for i in range(0, last_index):
            if nums[i] == val:
                return i

def test_removeElement():
    nums = [3, 3]
    val = 3
    assert Solution().removeElement(nums, val) == 0

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    assert Solution().removeElement(nums, val) == 5

    nums = [1]
    val = 1
    assert Solution().removeElement(nums, val) == 0

    nums = [1]
    val = 2
    assert Solution().removeElement(nums, val) == 1


if __name__ == '__main__':
    test_removeElement()
    print("classic27.py passed")