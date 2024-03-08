'''

3005. Count Elements With Maximum Frequency


You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

 https://leetcode.com/problems/count-elements-with-maximum-frequency/solutions/4840240/3005-count-elements-with-maximum-frequency-python

'''

class Solution(object):
    def maxFrequencyElements(self, nums):
        freq_counter = Counter(nums)
        
        max_frequency = max(freq_counter.values())

        max_freq_elements = [num for num, freq in freq_counter.items() if freq == max_frequency]

        total_frequency = max_frequency * len(max_freq_elements)

        return total_frequency