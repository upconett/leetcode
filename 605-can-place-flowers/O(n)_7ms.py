class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        awailable = 0
        i = 0
        while i < len(flowerbed):
            if (
                (flowerbed[i] == 0)
            and ((i==0) or flowerbed[i-1] == 0)
            and ((i==len(flowerbed)-1) or flowerbed[i+1] == 0) 
            ):
                awailable += 1
                i += 1
            i += 1
            if awailable >= n:
                return True
        return False
