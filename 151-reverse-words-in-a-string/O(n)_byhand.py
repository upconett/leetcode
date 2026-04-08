# That is essentially the same, but done by hand :D

class Solution:
    def reverseWords(self, s: str) -> str:
        sentance = self.split(s)
        sentance = self.reverse(sentance)
        return self.join(sentance)

        
    def split(self, s: str) -> list[str]:
        sentance = []
        word = ''
        for l in s:
            if l == ' ':
                if word != '':
                    sentance.append(word)
                    word = ''
            else:
                word += l
        if word != '':
            sentance.append(word)
        return sentance 

    def reverse(self, arr: list[str]) -> list[str]:
        new_arr = arr.copy()
        i = 0
        j = len(arr)-1
        while i < j:
            box = new_arr[i]
            new_arr[i] = new_arr[j]
            new_arr[j] = box
            i += 1
            j -= 1
        return new_arr

    def join(self, arr: list[str]) -> str:
        result = arr[0]
        for word in arr[1:]:
            result += ' '
            result += word
        return result
