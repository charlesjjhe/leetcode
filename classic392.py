class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        ti = 0
        while si < len(s):
            while ti < len(t):
                if s[si] == t[ti]:
                    si += 1
                    ti += 1
                else:
                    ti += 1
                if si >= len(s):
                    return True
            if ti >= len(t):
                return False
        return True


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    assert solution.isSubsequence("abc", "ahbgdc") == True
    assert solution.isSubsequence("axc", "ahbgdc") == False
    assert solution.isSubsequence("", "ahbgdc") == True
    assert solution.isSubsequence("abc", "") == False
    assert solution.isSubsequence("ace", "abcde") == True

    print("All test cases passed!")