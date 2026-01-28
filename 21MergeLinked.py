# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #cursors
        cursor1 = list1
        cursor2 = list2

        #head edge cases
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        #pick head of merged list (smaller of two heads)
        if list1.val <= list2.val: # break ties
            head = list1
            cursor1 = cursor1.next
        else:
            head = list2
            cursor2 = cursor2.next

        #cursor for merged linked list initialized at head
        cursorMerged = head


        while cursor1 is not None and cursor2 is not None:
            if cursor1.val <= cursor2.val:
                nextNode = cursor1
                cursor1 = cursor1.next
            else:
                nextNode = cursor2
                cursor2 = cursor2.next

            cursorMerged.next = nextNode
            cursorMerged = cursorMerged.next

        if cursor1 is None:
            cursorMerged.next = cursor2
        else:
            cursorMerged.next = cursor1

        return head

def main():
    s = Solution()
    #list1
    list13 = ListNode(4, None)
    list12 = ListNode(2, list13)
    list11 = ListNode(1, list12)

    #list2
    list23 = ListNode(4, None)
    list22 = ListNode(3, list23)
    list21 = ListNode(1, list22)

    sol = s.mergeTwoLists(list11,list21)
    #iterate & print
    while sol is not None:
        print(sol.val)
        sol = sol.next
    print(s.mergeTwoLists(list11,list21))
    #iterate

if __name__ == '__main__':
    main()




