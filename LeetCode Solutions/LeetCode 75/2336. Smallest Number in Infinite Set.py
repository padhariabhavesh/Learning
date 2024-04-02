'''

2336. Smallest Number in Infinite Set

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

    SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
    int popSmallest() Removes and returns the smallest integer contained in the infinite set.
    void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

    https://leetcode.com/problems/smallest-number-in-infinite-set/solutions/4960179/2336-smallest-number-in-infinite-set-python
'''

class SmallestInfiniteSet:
    def __init__(self):
        self.cur = 1
        self.s = set()

    def popSmallest(self):
        if self.s:
            res = min(self.s)
            self.s.remove(res)
            return res
        else:
            self.cur += 1
            return self.cur - 1

    def addBack(self, num):
        if self.cur > num:
            self.s.add(num) 

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)