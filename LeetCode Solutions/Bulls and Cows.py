"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        guess = list(guess)
        secret = list(secret)
        counter = collections.Counter(secret)
        a_counts, b_counts = 0, 0

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                counter[secret[i]] -= 1
                guess[i] = 'A'
                secret[i] = 'A'
                a_counts += 1

        for i in range(len(guess)):
            if guess[i] != 'A' and counter[guess[i]] > 0:
                counter[guess[i]] -= 1
                guess[i] = 'B'
                b_counts += 1

        return str(a_counts) + 'A' + str(b_counts) + 'B'