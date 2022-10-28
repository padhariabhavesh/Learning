"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""


class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        anagrams = dict()
        anagramGroups = []

        for string in strings:
            sortedString = "".join(sorted(string))
            stringList = anagrams.get(sortedString)

            if stringList is None:
                anagrams[sortedString] = []
            anagrams[sortedString].append(string)

        for sortedString in anagrams:
            anagramGroups.append(anagrams[sortedString])

        return anagramGroups