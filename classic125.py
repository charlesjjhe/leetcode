from pprint import pformat


class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        l = []
        for i in s:
            if i in t:
                l.append(str(i).lower())
            else:
                pass
        if len(l) == 0:
            return True
        # print(f'{l=}')
        return self.p(l, 0, len(l)-1)

    def p(self, l: list, h: int, t:int) -> bool:
        # print(f'{l[h]=}, {l[t]=}')
        if h == t:
            return True
        elif t - h == 1:
            if l[h] != l[t]:
                return False
            if l[h] == l[t]:
                return True
        else:
            if l[h] != l[t]:
                return False
            else:
                return self.p(l, h+1, t-1)


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    # assert solution.isPalindrome("") == True
    # assert solution.isPalindrome("a") == True
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True
    assert solution.isPalindrome("race a car") == False
    assert solution.isPalindrome("No 'x' in Nixon") == True
    assert solution.isPalindrome("12321") == True
    assert solution.isPalindrome("12345") == False

    print("All test cases passed!")