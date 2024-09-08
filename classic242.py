class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0] * 26
        aa = [0] * 26
        sl, tl = len(s), len(t)
        if sl != tl:
            return False
        i = 0
        while i < sl:
            si = ord(s[i]) - 97
            ti = ord(t[i]) - 97
            a[si] += 1
            a[ti] -= 1
            i += 1
        if a == aa:
            return True
        else:
            return False
