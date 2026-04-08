# That's the most lazy and eazy one

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([w for w in s.split(' ') if w][::-1])
