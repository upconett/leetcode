# I know I waste 1 integer extra space. That's my solution, I think it's neat >:)

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runningSum = [0]
        [runningSum.append(runningSum[i]+nums[i]) for i in range(len(nums))]
        return runningSum[1:]
