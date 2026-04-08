# 1071. Greatest Common Divisor of Strings
- https://leetcode.com/problems/greatest-common-divisor-of-strings

### Solution $O(n^2)$
The solution is based on no clever assumptions, although one optimisation.  
My chain of thoughts:
1. There should be a way to check if a substring is a divisor for another string
    - Thus, I've created a method `is_divisor`, that linearly could check that the `substr` is a divisor of `string`.
2. Then I should get every useful substring and check if it is a divisor for both strings
3. Then I should get the maximum length divisor from all of the filtered ones


### Solution $O(1)$
I believe that the solution is routhly in that complexity, but may be mistaken due to `gcd` method.  
The idea of the solution:
- The strings have common divisor if their contatenations are equal not matter the order of concatenation (e.g. `str1+str2 == str2+str1`)
- The greatest common divisor of these strings then is the substring of concatenation of length `gcd(len(str1), len(str2))`

It is a very neat trick, pity I did not see it >:(

