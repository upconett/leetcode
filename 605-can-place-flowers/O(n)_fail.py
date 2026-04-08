# Here I got in some wrong ways

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        awailable = 0
        i = 0
        while i <= len(flowerbed): 
            print(i, flowerbed[i:i+2], flowerbed[i-1:i+2], flowerbed[i-1:i+1])
            if (
                (i == 0)
                and (area := flowerbed[i:i+2]) 
                and (len(area) == 2)
                and (1 not in area)
            ):
                i += 1
                awailable += 1
            elif (
                (i == len(flowerbed)-1)
                and (area := flowerbed[i-1:i+1])
                and (len(area) == 2)
                and (1 not in area)
            ):
                awailable += 1
            elif (
                (area := flowerbed[i-1:i+2]) 
                and (len(area) == 3)
                and (1 not in area)
            ):
                i += 1
                awailable += 1
            if awailable >= n:
                return True
            i += 1
        return False
