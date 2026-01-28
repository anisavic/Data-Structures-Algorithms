# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #Floyd's Cycle
        if head is None:
            return False #edge case
        slow = head
        fast = head.next

        while fast is not None and slow != fast:
            try:
                fast = fast.next.next
            except AttributeError:
                fast = None
            try:
                slow = slow.next
            except AttributeError:
                slow = None


        if fast is None:
            return False
        else:
            return True



        #Valid, but too slow. hint: use Floyd's cycle algorithm
        # #Iterate over all nodes
        # node = head
        # while node is not None: #Iterate over nodes till we get to end
        #     #Iterate over all nodes up till node
        #     currPrevNode = head
        #     while currPrevNode != node:
        #         if node.next == currPrevNode:
        #             return True # Yes cycle! Node points to previous node
        #         currPrevNode = currPrevNode.next
        #
        #     node = node.next
        # return False # no cycle

def main():
    s = Solution()

    #define ex 3
    node1 = ListNode(1)
    print(s.hasCycle(node1))

    #define ex 2
    node1 = ListNode(1)
    node2 = ListNode(2)
    node2.next = node1
    node1.next = node2
    print(s.hasCycle(node1))

    #define ex 3
    node1 = ListNode(3)
    node2 = ListNode(3)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(s.hasCycle(node1))


if __name__ == '__main__':
    main()

