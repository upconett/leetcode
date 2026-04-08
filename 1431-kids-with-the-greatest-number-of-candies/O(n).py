class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maximum = max(candies)
        return [True if c+extraCandies >= maximum else False for c in candies]