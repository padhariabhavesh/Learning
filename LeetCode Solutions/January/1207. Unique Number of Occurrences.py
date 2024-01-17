'''
1207. Unique Number of Occurrences
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        list_hashmap = list(hashmap.values())
        count_hashmap = {}
        for i in list_hashmap:
            if i in count_hashmap:
                return False        