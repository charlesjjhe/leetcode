from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nl = len(nums)
        i = 0
        ndict = {}
        while i < nl:
            nstr = str(nums[i])
            if nstr not in ndict.keys():
                ndict[nstr] = [i]
            else:
                ndict[nstr].append(i)
            i += 1
        for k in ndict.keys():
            tk = int(target - int(k))
            kk = str(tk)
            print(f'{k=}, {kk=}')
            if kk == k:
                if len(ndict[k]) >= 2:
                    return ndict[k][0:2]
            else:
                if kk in ndict.keys():
                    return [ndict[k][0], ndict[kk][0]]
        return []

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    assert solution.twoSum([1, 2, 3, 4, 5], 10) == []
    assert solution.twoSum([0, 4, 3, 0], 0) == [0, 3]