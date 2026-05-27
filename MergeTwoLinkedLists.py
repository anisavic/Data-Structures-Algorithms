# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        make a dummy node so it is the head of list, this
        is the starting point where we stitch the list together
        if dummy->
        and list1 = [1,2,4]
        and list2 = [1,3,5]
        dummy->1, then replace list1 = [2,4]
        dummy->1->1, replace list2=[3,5]
        dummy->1->1->2 (list1 is less than equal to) then replace list1=[4]
        dummy->1->1->2->3 (list2 is greater than list1) then replace list2=[5]
        dummy->1->1->2->3->4 (list1 is greater than list2), then replace list1=[]
        list1 is None, so now attatch to what remains

        point dummy's next to whichever one is smaller of the heads,
        reassign heads of list1 or list2 to next until one of them is null, in which case
        we attatch the remainder of the list

        need a dummy, and a current and keep track of list1 and list2 (they are the heads)

        dummy -> None
        current = dummy

        while both of them are still nonempty:
            take next to be higher of the two (list1orlist2)
            move either list1 or list2 forward accordingly
            set currents next to next
            move current up
        
        take nonempty one (if there is one) and set current next to the head of list

        improvements:
        -remove redundant next variable and just wire it into currents next
        -one liner truthy assignment to append remaining values to list

        truthy: objects with "true" value based on their nature (nonempty list, positive number, etc)
        falsy: emoty array, 0, None
        by logic of A or B, if A truthy returns A, otherwise fallback to B
        """
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
 
            current = current.next
        
        # either one or both of them are now empty, append remaining to currents next
        current.next = list1 or list2

        return dummy.next

if __name__ == "__main__":
    t = Solution()
    node3 = ListNode(4, None)
    node2 = ListNode(2, node3)
    list1 = ListNode(1, node2)


    node6 = ListNode(5, None)
    node5 = ListNode(3, node6)
    list2 = ListNode(1, node5) 

    print(t.mergeTwoLists(list1, list2))