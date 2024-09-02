class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        i = 0
        t = -1
        si, ei = 0, 0
        # while i < l:
        #     if s[i] != ' ':
        #         si = i
        #         break
        #     i += 1
        i = l - 1
        while i >=0:
            if s[i] != ' ':
                ei = i
                break
            i -= 1
        print(f'{si=}, {ei=}')
        if si == ei:
            return 1
        while si <= ei:
            if s[si] == ' ':
                t = si
            si += 1
        print(f'{t=}')
        return ei - t

if __name__ == '__main__':
    s = Solution()
    st = "   fly me   to   the moon  "
    print(s.lengthOfLastWord(st))

    st = " aaa"
    print(s.lengthOfLastWord(st))

    st = "aaa "
    print(s.lengthOfLastWord(st))