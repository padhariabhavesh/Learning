'''
Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.


https://youtu.be/yjunnR2wDh0
'''

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a = 0
        # Step 1: Relative Ordering
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    arr1[a], arr1[j] = arr1[j], arr1[a]
                    a += 1
        # Step 2: Sorting Remaining Elements
        arr1[a:] = sorted(arr1[a:])
        return arr1