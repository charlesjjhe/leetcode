from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        i = 0
        d1 = {}
        while i < len(nums):
            e = str(nums[i])
            if e in d1.keys() and i - d1[e] <= k:
                return True
            else:
                d1[e] = i
                i += 1
        return False

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
    assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1) == True
    assert solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
    assert solution.containsNearbyDuplicate([1, 2, 3, 4, 5], 0) == False
    assert solution.containsNearbyDuplicate([], 1) == False

    print("All test cases passed!")