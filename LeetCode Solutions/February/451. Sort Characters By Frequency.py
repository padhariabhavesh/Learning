'''
451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
'''



class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        pq = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(pq)
        result = ''
        while pq:
            freq, char = heapq.heappop(pq)
            result += char * -freq
        return result


