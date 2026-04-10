class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 == str2+str1:
            gcd = self.gcd(len(str1), len(str2))
            return (str1+str2)[:gcd]
        return ''

    def gcd(self, a: int, b: int) -> int:
        for i in range(min(a, b)+1, 0, -1):
            if a % i == b % i == 0:
                return i
        return 1
