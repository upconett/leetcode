# 1480. Running Sum of 1d Array
- https://leetcode.com/problems/running-sum-of-1d-array
- Difficulty: 🟩 EASY
- Topics: `Mid Level` `Array` `Prefix Sum` `Weekly Contest 193`

### Solution $O(n)$ [🔗](./O(n).py)
- The idea is, that we don't need to recalculate the whole sum for each index
- Instead we use the sum on the previous index, and add the new number to it
- That's that simple
