from time import sleep


class Solution:
    def reverseWords(self, s: str) -> str:
        start = 0
        reversedS = ''
        while start < len(s):
            end = start
            while end < len(s) and s[end] != ' ':
                end += 1
            for i in range(end - start):
                reversedS += s[end - 1 - i]

            start = end + 1
            if start < len(s):
                reversedS += ' '

        return reversedS

def reverseWords(s):
    print('*************************')
    print(s)
    solution = Solution()
    result = solution.reverseWords(s)
    print(result)
    return result

assert reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc", 'First'
assert reverseWords("God Ding") == "doG gniD", 'Second'
assert reverseWords("Words") == "sdroW", 'Only a word'
assert reverseWords("Three string words") == "eerhT gnirts sdrow", 'Three words'