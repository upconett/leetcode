class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = 'aeiou'
        sarr = list(s)
        i = 0
        j = len(sarr)-1
        while i < j:
            while i < len(sarr) and s[i].lower() not in VOWELS:
                i += 1
            while j > 0 and s[j].lower() not in VOWELS:
                j -= 1
            if i >= j:
                break
            self.swap(sarr, i, j)
            i += 1
            j -= 1
        return ''.join(sarr)

    def swap(self, sarr: list[str], i: int, j: int):
        a = sarr[i]
        sarr[i] = sarr[j]
        sarr[j] = a
