'''
1481. Least Number of Unique Integers after K Removals

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
'''

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)

        sorted_freq = sorted(freq_map.items(), key=lambda x: x[1])

        for num, freq in sorted_freq:
            if k >= freq:
                k -= freq
                del freq_map[num]
            else:
                break

        return len(freq_map) 