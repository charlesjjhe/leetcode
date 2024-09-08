from collections import OrderedDict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sod = self.god(pattern)
        tod = self.god(s, pf=True)
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

    def god(self, s: str, pf: bool = False) -> OrderedDict:
        od = OrderedDict()
        if pf:
            s = s.split(' ')
        si = 0
        while si < len(s):
            t = s[si]
            if t not in od.keys():
                tl = [si]
                od.update({t: tl})
            else:
                od.get(t).append(si)
            si += 1
        return od