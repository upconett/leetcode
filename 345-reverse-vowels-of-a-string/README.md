# 345. Reverse Vowels of a String
- https://leetcode.com/problems/reverse-vowels-of-a-string
- Difficulty: 🟩 EASY
- Topics: `Two Pointers` `String`
- From [Leetcode 75](https://leetcode.com/studyplan/leetcode-75)

### Solution $O(n)$ (182ms) [🔗](./O(n)_182ms.py)
- Done in `00:06:58`
- On my first attempt, I've tried to iterate over the string, saving the parts with consonants and parts with vowels
- The vowels were stored in reverse order `vow_parts.insert(0, l)`, the consonants regularly (via `append`)
- Then I've rebuilt the string by alternating the vowel parts and consonant parts


### Solution $O(n)$ (19ms) [🔗](./O(n)_19ms.py)
- The only change is that instead of doing `vow_parts.insert(0, l)` I've done `vow_parts.append(l)` and then reversed at the moment of rebuilding the string: `reversed += vow_parts[len(vow_parts-i-1)]`
- But my solution still requires a lot of memory (21.49mb)


### Solution $O(n)$ (15ms) (7ms) [1🔗](./O(n)_15ms.py) [2🔗](./O(n)_7ms.py)
- I am using 2 pointers (which I peaked from the Topics section of the task)
- The pointers `i` and `j` are going from the start and the end of the string respectively
- If the pointer finds a vowel, it stays in place waiting for another pointer
- When both pointers find vowels, these vowels are swapped
- If the pointers met, we stop the loop

- There are two approaches to moving pointers `15ms` ([1🔗](./O(n)_15ms.py)) and `7ms` ([2🔗](./O(n)_7ms.py))
