class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s[:]
            minc = s[0]
            for x in range(len(s)):
                if s[x] <= minc:
                    minc = s[x]
                    ans = min(ans, s[x:]+s[:x])
            return ans
        return ''.join(sorted(list(s)))