# fails with time limit exceeded

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            result.append(self.mul(nums[:i]+nums[i+1:]))
        return result
    
    def mul(self, nums: list[int]) -> int:
        result = 1
        for a in nums:
            result *= a
        return result
