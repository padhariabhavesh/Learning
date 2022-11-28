"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
"""

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win=dict()
        lose=dict()
        for x in matches:
            if x[0] not in win.keys():
                win[x[0]]=1
            else:
                win[x[0]]+=1
            if x[1] not in lose.keys():
                lose[x[1]]=1
            else:
                lose[x[1]]+=1
        re=[[],[]]
        for x in lose.keys():
            if lose[x]==1:
                re[1].append(x)
        for x in win.keys():
            if x not in lose.keys():
                re[0].append(x)
        re[0].sort()
        re[1].sort()
        return re