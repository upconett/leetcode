class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        awailable = 0
        i = 0
        while i < len(flowerbed):
            before = flowerbed[i-1] if (i > 0) else 0
            after = flowerbed[i+1] if (i < len(flowerbed)-1) else 0
            plot = flowerbed[i]
            if before+after+plot == 0:
                awailable += 1
                i += 1
            i += 1
            if awailable >= n:
                return True
        return False
