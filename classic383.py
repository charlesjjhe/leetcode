class Solution:
    def canConstruct_v1(self, ransomNote: str, magazine: str) -> bool:
        md = {}
        for i in magazine:
            if i not in md.keys():
                md[i]=1
            else:
                md[i] += 1
        for r in ransomNote:
            if r in md.keys():
                if md[r] > 0:
                    md[r] -= 1
                else:
                    return False
            else:
                return False
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ml = [0]*26
        for i in magazine:
            ml[ord(i)-97] += 1
        for r in ransomNote:
            mi = ord(r) - 97
            if ml[mi] > 0:
                ml[mi] -= 1
            else:
                return False
        return True

