# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        cycle detection, slow and fast pointers
        1   2   3   4   5
            |   _   _   |
        slow and fast pointer, keep going until they point to same node
        if same, cycle detected!
        if encounter a None, false!

        slow = head
        fast = head

        while fast:
            slow = slow.next
            fast = fast.next.next # possible problem here?
            if slow equals fast:
                cycle! return True
        
        fast encountered end of list, no cycle so False

        problem in fast.next.next since may reach none, who has no .next
        value after that
        if fast.next it is safe else return False since no cycle, end of list?

        fix: avoid this by checking both fast and fast next in while condition before assigning
        this ensures that if we reach end, there is no cycle and correctly return false
        '''

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        