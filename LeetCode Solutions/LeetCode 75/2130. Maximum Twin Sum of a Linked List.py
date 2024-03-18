'''

2130. Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

    For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.

The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/solutions/4893158/2130-maximum-twin-sum-of-a-linked-list-python
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # First, we count of many nodes there are
        pointer = head
        count = 0
        while pointer:
            pointer = pointer.next
            count += 1
        
        # Find the middle by floor division
        middle = count // 2

        # Create second linked list from middle:
        half = None
        curr = head
        track = 0 
        while curr:
            if track == middle:
                half = curr
            curr = curr.next
            track += 1

        # Reverse the half
        reversed_half = None
        curr_half = half
        while curr_half:
            nxt = curr_half.next
            curr_half.next = reversed_half
            reversed_half = curr_half
            curr_half = nxt
        
        # Compute sums and find result
        result = 0
        original = head
        while reversed_half:
            curr_sum = reversed_half.val + original.val
            result = max(result, curr_sum)
            reversed_half = reversed_half.next
            original = original.next

        return result
 