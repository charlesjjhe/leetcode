class Solution:
    def isValid(self, s: str) -> bool:
        l = [s[0]]
        m = {')':'(', '}':'{', ']':'['}
        for c in s[1:]:
            if c not in m:
                l.append(c)
            else:
                if len(l) == 0:
                    return False
                if l[-1] == m[c]:
                    l.pop()
                else:
                    return False
        if len(l) > 0:
            return False
        else:
            return True
