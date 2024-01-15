'''
2225. Find Players With Zero or One Losses

You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

    answer[0] is a list of all players that have not lost any matches.
    answer[1] is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.

Note:

    You should only consider the players that have played at least one match.
    The testcases will be generated such that no two matches will have the same outcome.

Check Here: https://leetcode.com/problems/find-players-with-zero-or-one-losses/solutions/4570749/2225-find-players-with-zero-or-one-losses-python

'''

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}

        players = set()

        answer = [[], []]

        for winner, loser in matches:
            if winner  not in players:
                players.add(winner)

            if loser not in players:
                players.add(loser)
        
            winners[winner] = winners.get(winner, 0) + 1
            losers[loser] = losers.get(loser, 0) + 1

        for player in players:
            if player not in losers:
                answer[0].append(player)
            elif losers.get(player, 0) == 1:
                answer[1].append(player)

        return [sorted(answer[0]), sorted(answer[1])]        