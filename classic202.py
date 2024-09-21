class Solution:
    def isHappy(self, n: int) -> bool:
        nset = set()
        while 1==1:
            nset.add(n)
            nstr = str(n)
            n = 0
            for i in nstr:
                n += (int(i) * int(i))
            if n == 1:
                return True
            elif n in nset:
                return False