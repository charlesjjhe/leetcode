from collections import OrderedDict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)
        if sl != tl:
            return False
        sod = self.god(s)
        tod = self.god(t)
        sodk = len(sod.keys())
        todk = len(tod.keys())
        if sodk != todk:
            return False
        i = 0
        while i < sodk:
            sodkv = sod.popitem(last=False)[1]
            todkv = tod.popitem(last=False)[1]
            if sodkv == todkv:
                i += 1
                pass
            else:
                return False
        return True

    def god(self, s: str) -> OrderedDict:
        od = OrderedDict()
        si = 0
        while si < len(s):
            t = s[si]
            if t not in od.keys():
                tl = [si]
                od.update({t:tl})
            else:
                od.get(t).append(si)
            si += 1
        return od


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    assert solution.isIsomorphic("egg", "add") == True
    assert solution.isIsomorphic("foo", "bar") == False
    assert solution.isIsomorphic("paper", "title") == True
    assert solution.isIsomorphic("ab", "aa") == False
    assert solution.isIsomorphic("", "") == True

    print("All test cases passed!")