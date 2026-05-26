# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 4 step: 
        '''
        hold next from curr.next
        current's next becomes prev (reverse step)
        prev becomes curr (slide prev up)
        curr becomes next (slide curr up)
        reverse list and return head
        start curr at head, and while curr.next exists, keep going.
        when curr.next is none we have reached end and list will be reversed


        set prev to head
        set curr to head.next

        while curr.next exists:
            store current's next as nxt
            set currents nxt to prev
            slide prev up to curr
            slide curr up to next
        
        return curr
        '''

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        
        return prev


if __name__ == "__main__":
    t = Solution()
    test = [0,1,2,3]
    print(t.reverseList(test))