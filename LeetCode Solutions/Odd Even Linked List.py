"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        odd_head = ListNode(0)
        odd = odd_head

        even_head = ListNode(0)
        even = even_head

        count = 0
        while head != None:
            if count % 2 == 0:
                odd.next = head
                odd = head
            else:
                even.next = head
                even = head

            count += 1
            head = head.next

        even.next = None
        odd.next = even_head.next

        return odd_head.next