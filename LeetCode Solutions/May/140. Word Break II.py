'''

140. Word Break II


Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        @cache
        def helper(t):
            combos = []
            if not t:
                return [""]
            for i, _ in enumerate(t):
                w = t[:i+1] 
                if w in wordSet:
                    combos.extend([
                        f'{w} {sentence}' if sentence else w 
                        for sentence in helper(t[i+1:])
                    ])
            return combos
        return helper(s)