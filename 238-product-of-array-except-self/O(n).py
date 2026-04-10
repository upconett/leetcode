class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pref = [1, nums[0]]   # prefix  multiplications
        post = [1, nums[-1]]  # postfix multiplications

        for i in range(1, len(nums)-1):
            pref.append(pref[i]*nums[i])
            post.append(post[i]*nums[-(i+1)])

        result = []
        for i in range(len(nums)):
            result.append(pref[i]*post[-(i+1)])

        return result
