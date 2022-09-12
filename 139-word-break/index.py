# dynamic programming, backtracking, string

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordBreakDict = {}
    
        def workBreakBacktrack(s: str) -> bool:
            if s == "":
                return True

            for word in wordDict:
                if s.startswith(word):
                    remainS = s[len(word):]
                    if remainS not in wordBreakDict.keys():
                        wordBreakDict[remainS] = workBreakBacktrack(remainS)
                    if wordBreakDict[remainS]:
                        return True

            return False
        
        return workBreakBacktrack(s)
        

def wordBreak(s: str, wordDict: List[str]) -> bool:
    global i
    i = 0
    print('***************************')
    print(s, wordDict)
    sls = Solution()
    result = sls.wordBreak(s, wordDict)
    print('--------------')
    print(result)
    return result

assert wordBreak("catanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatanddogcatsandog", ["cats","dog","sand","and","cat"]) == False
assert wordBreak("leetcode", ["leet","code"]) == True
assert wordBreak("applepenapple", ["apple","pen"]) == True
assert wordBreak("catsandog", ["cats","dog","sand","and","cat"]) == False
assert wordBreak("catanddogcatdogeand", ["cat", "and", "dog", "e"]) == True
assert wordBreak("catanddogcatdogeand", ["cat", "and", "dog"]) == False
assert wordBreak("babysharkhehe", ["hehe", "shark", "bab", "yshar"]) == False
assert wordBreak("cars", ["car","ca","rs"]) == True
assert wordBreak("catsandog", ["cats", "sand", "dog", "cat"]) == False
assert wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) == False