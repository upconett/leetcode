class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = 'aeiou'
        sarr = list(s)
        i = 0
        j = len(sarr)-1
        ifound = jfound = False
        while i < j:
            if not ifound and sarr[i].lower() in VOWELS:
                ifound = True
            if not jfound and sarr[j].lower() in VOWELS:
                jfound = True
            if ifound and jfound:
                self.swap(sarr, i, j)       
                ifound = jfound = False
            if not ifound:
                i += 1
            if not jfound:
                j -= 1
        return ''.join(sarr)

    def swap(self, sarr: list[str], i: int, j: int):
        a = sarr[i]
        sarr[i] = sarr[j]
        sarr[j] = a
