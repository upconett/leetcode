class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        max_divisor = ''
        shorter = str1 if len(str1) <= len(str2) else str2
        longer = str2 if str1 is shorter else str1
        
        for i in range(1, len(shorter)+1):
            if len(shorter) % i:
                continue
            lss = len(shorter) // i
            substr = shorter[:lss]
            if self.is_divisor(shorter, substr) and self.is_divisor(longer, substr):
                if len(substr) > len(max_divisor):
                    max_divisor = substr

        return max_divisor

    def is_divisor(self, string: str, substr: str) -> bool:
        ratio = len(string)/len(substr)
        if ratio != int(ratio):
            return False
        ratio = int(ratio)
        if ratio == 1:
            return string == substr
        for i in range(1, ratio+1):
            a = len(substr)*(i-1)
            b = len(substr)*i
            if string[a:b] != substr:
                return False
        return True
