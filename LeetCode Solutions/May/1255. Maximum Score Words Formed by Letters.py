'''

1255. Maximum Score Words Formed by Letters


Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.


'''

class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        lettersCounter = Counter(letters)
        totalScore = 0

        def explore(index, letterCounter, currScore):
            nonlocal totalScore

            totalScore = max(totalScore, currScore)
            if index == len(words):
                return

            for i in range(index, len(words)):
                tmpCounter = copy.deepcopy(letterCounter)
                word = words[i]
                wordScore = 0
                isValid = True

                for ch in word:
                    if ch in tmpCounter and tmpCounter[ch] > 0:
                        tmpCounter[ch] -= 1
                        wordScore += score[ord(ch) - ord("a")]
                    else:
                        isValid = False
                        break
                if isValid:
                    explore(i + 1, tmpCounter, currScore + wordScore)

        explore(0, lettersCounter, 0)
        return totalScore
