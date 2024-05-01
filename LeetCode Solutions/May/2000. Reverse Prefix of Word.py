'''

2000. Reverse Prefix of Word

Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

    For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".

Return the resulting string.

https://leetcode.com/problems/reverse-prefix-of-word/solutions/5093674/2000-reverse-prefix-of-word-python
'''

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        indexch = word.index(ch)
        return word[indexch::-1] + word[indexch+1::]
        