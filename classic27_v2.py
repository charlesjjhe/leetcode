from typing import List

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        d = []
        for i in range(0, len(nums)):
            if nums[i] != val:
                d.append(nums[i])
        for i in range(0, len(d)):
            nums[i] = d[i]
        return len(d)


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