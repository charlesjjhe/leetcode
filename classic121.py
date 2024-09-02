# TODO not done lar

from typing import List

class Solution:
    # in this way, will time out
    def maxProfit_v1(self, prices: List[int]) -> int:
        l = len(prices)
        if l == 1:
            return 0
        if l == 2:
            if prices[0] >= prices[1]:
                return 0
            else:
                return prices[1] - prices[0]
        m = 0
        for i in range(0, l - 1):
            for ii in range(i, l-1):
                a = prices[ii + 1] - prices[i]
                m = a if m < a else m
        return m

    # O(n)
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

if __name__ == "__main__":
    s = Solution()
    p = [7,1,5,3,6,4]
    s.maxProfit(p)