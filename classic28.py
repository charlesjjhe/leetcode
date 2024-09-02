class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hl = len(haystack)
        nl = len(needle)
        for i in range(0, hl):
            if needle[0] == haystack[i]:
                if needle == haystack[i:i+nl]:
                    return i
        return -1


if __name__ == '__main__':
    s = Solution()

    h = "leetcode"
    n = "leeto"
    print(s.strStr(h, n))

    h = "sadbutsad"
    n = 'sad'
    print(s.strStr(h, n))