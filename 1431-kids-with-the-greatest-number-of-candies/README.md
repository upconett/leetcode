# 1431. Kids With the Greatest Number of Candies
- https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
- Difficulty: 🟩 EASY
- Topics: `Mid Level` `Array` `Biweekly Contest 25`
- From [Leetcode 75](https://leetcode.com/studyplan/leetcode-75)

Well, after the [1071.](https://github.com/upconett/leetcode/tree/main/1071-greatest-common-divisor-of-strings) I was kinda disappointed

### Solution $O(n)$ [🔗](./O(n).py)
No clever trick required:
- We just store the `maximum` number of candies from initial list
- Then build a new list iterating over the initial one (with `i` index):
    - For each kid, we check if `candies[i]+extraCandies` is less than or equal to `maximum`
    - If so, store `True`, otherwise `False`

Solved in about 3 minutes 🤨