'''
1897. Redistribute Characters to Make All Strings Equal using Python

You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.

Link : https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/solutions/4478206/1897-redistribute-characters-to-make-all-strings-equal-using-python/

'''


class Solution:
    def makeEqual(self,  words: List[str]) -> bool:
        char_cnt = defaultdict(int)

        for w in words:
            for c in w:
                char_cnt[c] +=1

        for c in char_cnt:
            if char_cnt[c] % len(words):
                return False
        return True
    

    