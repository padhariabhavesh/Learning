'''

2487. Remove Nodes From Linked List


You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

https://leetcode.com/problems/remove-nodes-from-linked-list/solutions/5118633/2487-remove-nodes-from-linked-list-python

'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        stack = []
        while cur:
            while stack and stack[-1].val < cur.val:
                a = stack.pop()
            stack.append(cur)
            cur = cur.next
        
        nxt = None
        while stack:
            cur = stack.pop()
            cur.next = nxt
            nxt = cur
        
        return cur