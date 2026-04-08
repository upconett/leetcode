# 605. Can Place Flowers
- https://leetcode.com/problems/can-place-flowers
- Difficulty: 🟩 EASY
- Topics: `Senior` `Array` `Greedy`
- From [Leetcode 75](https://leetcode.com/studyplan/leetcode-75)

### Solution $O(n)$ (80ms)
- Done in `00:06:24`
- On my first attempt, I've tried to add padding to the list and simply iterate through the flowerbed
- Then I've checked if places around and at my iterator `i` are equal to `0`
- If so, I've "planted" a flower there and incremented `awailable` counter
- If the `awailable` is already enough to fulfill the `n`, I return `True`
- If the `awailable` is not enought after the loop, I return `False`


### Solution $O(n)$ (12ms)
- To reduse the space and time complexity I've decided not to update the `flowerbed` array, e.g. no padding and no "planting" the flowers
- Instead of padding I've added checks for `i` being on edges of array
- Instead of "planting" I am now leaping 2 units (`i+=1;i+=1`) if the plot is suitable for the plant
    - The reasoning for this: the plant is impossible to "plant" immedietelly onto the next plot after the currently "planted" one, so instead of "planting", I could just skip the next plot, checking the second next one instead
- This approach decreases the time and space complexity because I don't need to juggle the array, and everything is in place


### Solution $O(n)$ (7ms) BEST I'VE GOT
- To further optimize the solution, I've dropped the additional variables
- Instead I've comprised a single if statement, that universally checks if the current plot is awailable
- If the statement is `True` I do the `i+=1` leaping and `awailable` increment
- Somehow that helped to get another couply of milliseconds
