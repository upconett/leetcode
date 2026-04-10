class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            if (wealth := sum(account)) > max_wealth:
                max_wealth = wealth
        return max_wealth
