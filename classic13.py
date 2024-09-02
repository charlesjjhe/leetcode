class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        dd = {'IV': 4, 'IX':9, 'XL': 40, 'XC':90, 'CD':400, 'CM':900}
        if s in dd.keys():
            return dd[s]
        if s in d.keys():
            return d[s]
        i = 0
        ret = 0
        while i < (len(s) - 1):
            if s[i]+s[i+1] in dd.keys():
                ret += dd[s[i]+s[i+1]]
                i += 2
            else:
                ret += d[s[i]]
                i += 1
        if i == len(s) - 1:
            ret += d[s[i]]
        return ret



if __name__ == '__main__':
    s = Solution()

    t1 = 'III'
    print(s.romanToInt(t1))