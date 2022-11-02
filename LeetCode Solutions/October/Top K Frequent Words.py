"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        results = []

        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1

        heap = []
        for key, value in count.items():
            heapq.heappush(heap, (-value, key))

        for i in range(k):
            results.append(heapq.heappop(heap)[1])

        return results

