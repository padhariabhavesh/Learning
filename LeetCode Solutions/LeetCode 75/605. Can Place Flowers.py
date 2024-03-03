'''
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
https://leetcode.com/problems/can-place-flowers/solutions/4813442/605-can-place-flowers-python
 
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0,0)
        flowerbed.append(0)
        for i in range(1,len(flowerbed)-1):
            if n==0:
                return True
            else: 
                if flowerbed[i]+flowerbed[i+1]==0 and flowerbed[i-1]!=1:
                    flowerbed[i]=1
                    n-=1
        return n<=0
        