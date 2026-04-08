class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = 'aeiou'
        con_parts = []
        vow_parts = []
        con = ''
        for l in s:
            if l.lower() in VOWELS:
                vow_parts.append(l)
                con_parts.append(con)
                con = ''
            else:
                con += l
        con_parts.append(con)
        reversed = con_parts[0]
        for i in range(len(vow_parts)):
            reversed += vow_parts[len(vow_parts)-i-1]
            reversed += con_parts[i+1]
        return reversed
