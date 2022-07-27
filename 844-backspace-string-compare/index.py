class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for chr in s:
            if chr == '#':
                if len(stack1) > 0:
                    stack1.pop()
            else:
                stack1.append(chr)

        stack2 = []
        for chr in t:
            if chr == '#':
                if len(stack2) > 0:
                    stack2.pop()
            else:
                stack2.append(chr)
        
        return stack1 == stack2

def backspaceCompare(s: str, t: str) -> bool:
    print('**************************')
    print(s,t)
    solution = Solution()
    result = solution.backspaceCompare(s,t)
    print(result)
    return result

assert backspaceCompare("ab#c", "ad#c") == True, 'First'
assert backspaceCompare("ab##", "c#d#") == True, 'Second'
assert backspaceCompare("a#c", "b") == False, 'Third'
assert backspaceCompare("acc##", "b#d#a") == True, 'Fourth'
assert backspaceCompare("", "") == True, 'Emmty string'
assert backspaceCompare("a##c", "#a#c") == True, 'Pop empty string'
assert backspaceCompare("ab", "cabb#") == False, 'len t > len s'