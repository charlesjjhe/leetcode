from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = ""
        l = len(strs)
        if l == 0:
            return t
        elif l == 1:
            return strs[0]
        fw = strs[0]
        wi = 0
        cf = True
        while wi < len(fw) and cf:
            i = 0
            while i < len(strs):
                if wi == len(strs[i]):
                    cf = False
                    break
                if fw[wi] == strs[i][wi]:
                    i += 1
                else:
                    cf = False
                    break
            if i == len(strs):
                t += fw[wi]
            wi += 1
        return t


