class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        awailable = 0
        flowerbed = [0, *flowerbed, 0]
        for i in range(1, len(flowerbed)-1):
            prev, plot, next = flowerbed[i-1:i+2]
            if prev == plot == next == 0:
                flowerbed[i] = 1
                awailable += 1
            if awailable >= n:
                return True
        return False
