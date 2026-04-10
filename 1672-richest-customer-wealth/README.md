# 1672. Richest Customer Wealth
- https://leetcode.com/problems/richest-customer-wealth
- Difficulty: 🟩 EASY
- Topics: `Mid Level` `Array` `Matrix` `Weekly Contest 217`

### Solution $O(n)$
Solution requires to compute the sum of account money across all banks and save the largest result of the computation

For each `account` in given `accounts` list, we need to compute the `sum(account)`, store the result in `wealth` variable and compare it to `max_wealth`.  
If the `wealth` of current `account` is larger than `max_wealth` (that is 0 by default), we assign `max_wealth = wealth`.  
After the loop exit, we got to return the `max_wealth` found accross all the `accounts` in $O(n)$ time-complexity.
