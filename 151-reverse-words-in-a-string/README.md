# 151. Reverse Words in a String
- https://leetcode.com/problems/reverse-words-in-a-string
- Difficulty: 🟨 MEDIUM (why? idk)
- Topics: `Two Pointers` `String`
- From [Leetcode 75](https://leetcode.com/studyplan/leetcode-75)

That's dead simple, I don't even know why it is a **Medium** one

### Solution $O(n)$
- You first split the string, removing unwanted spaces
- Then you reverse the string, I've done it using 2 pointers (see `O(n)_byhand.py`)
- The you join the string back together, and return it
