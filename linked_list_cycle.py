# Given a linked list, return the node where the cycle begins. 
# If there is no cycle, return null.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        # traverse the LL
        current = head
        while current is not None:
            # If we find a node with the visited property,
            # return that node
            if hasattr(current, 'visited'):
                return current
            else:
                # Add visited property, traverse
                current.visited = True
                current = current.next
        # If no cycle, return null
        return null