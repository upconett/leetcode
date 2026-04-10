# 238. Product of Array Except Self
- https://leetcode.com/problems/product-of-array-except-self
- Difficulty: 🟨 MEDIUM
- Topics: `Array` `Prefix Sum`
- From [Leetcode 75](https://leetcode.com/studyplan/leetcode-75)

### Solution $O(n^2)$ [🔗](./O(n**2)_fail.py) (failed due to time limit)
- My first shot was straitforward, I've just multiplied everything out
- The answer should have been correct, but the algorithm is unoptimized, which I understand

### Solution $O(n)$ [🔗](./O(n).py)
That's working, and I love it (cause looking clean)  
The idea is, I'm precomputing the multiplications in a separate lists, then to reause the results

I'll explain on an example:
- Input:  `[1,2,3,4]`
- Output: `[24,12,8,6]`

First I compute the `pref` list (list of multiplications going from first to last elements)
Like that: `[1, 1*2, 1*2*3]`, i.e. `[1, 2, 6]`
- I don't compute the last `1*2*3*4` cause we always multiply `n-1` numbers (that's "except self")

Then I compute the `post` list (list of multiplications going from last to first elements)
- Like that: `[4, 4*3, 4*3*2]`, i.e. `[4, 12, 24]`

And then I reverse the `post` list, cause it was assembled in reverse (from last to first el.)
- So that I have `post=[24,12,4]`

Thus I have all the required parts to assemble each multiplication
The meaning of the `post` and `pref` lists are the multiplications of everything in `nums` with accumulated result
- Thus `24` in `post` list represents the mul. of all the numbers except the `i=0` in `nums`
- And `6` in `pref` list represents the mul. of all the numbers except the `i=3` in `nums`

But how to get the result for `i=1` and `i=2`?
- For `i=1`, we should multiply `1 * 3 * 4`, which is `1 * 12`
    - `1` is stored in `pref` list, as prefix multiplication of all elements before `i=1` (at `i=0`)
    - `12` is stored in `post` list as postfix multiplication of all elements after `i=1` (at `i=1`)
- For `i=2`, we should multiply `1 * 2 * 4`, which is `2 * 4`
    - `2` is in `pref` at index `i=1`
    - `4` is in `post` at index `i=2`

The solution could be neatly depicted as so:
```python
     i  0  1  2  3
  nums [1, 2, 3, 4]
  
  pref    [1, 2, 6]
           *  * 
  post [24,12,4]
        =  =  =  =
result [24,12,8, 6]
```
The `pref` list is shifted one index to the right, you see?
- That is because we always use `i-1` index for it in our computation (see previous discussion)
- To remove the inconsistency in indexes (having to shift `i-1` for `pref`) and in operations (having to multiply only for `0<i<len(nums)-1`) we can insert `1`s in our arrays to fill in the gaps

Add `1` at the start of `pref` and at the end of `post`   
```python
     i  0  1  2  3
  nums [1, 2, 3, 4]
         
  pref [1, 1, 2, 6]
        *  *  *  *
  post [24,12,4, 1]
        =  =  =  =
result [24,12,8, 6]
```
Thus result for each `nums[i]` could be composed by `pref[i] * post[i]`, isn't it beautiful?
- In the code, I remove the inconsistency by initialising the arrays with `1` as the first value and then reverse the `post` list
```python
pref = [1, nums[0]]   # prefix  multiplications
post = [1, nums[-1]]  # postfix multiplications
```
- Then I fill in both of the multiplications lists:
```python
for i in range(1, len(nums)-1):
    pref.append(pref[i]*nums[i])
    post.append(post[i]*nums[-(i+1)])
```
- Then I compose the result (but use back-indexing `-(i+1)` for `post` list instead of inverting it to gain a bit of performance):
```python
result = []
for i in range(len(nums)):
    result.append(pref[i]*post[-(i+1)])
```