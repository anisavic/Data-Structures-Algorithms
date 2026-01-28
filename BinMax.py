# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if(root is None):
            return 0
        if(root.left is None and root.right is None): #base case
            return 1
        else: #recursive case
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def main():
    s = Solution()
    fifteen = TreeNode(15, None, None)
    seven = TreeNode(7, None, None)
    twenty = TreeNode(20, fifteen, seven)
    nine = TreeNode(9, None, None)
    root = TreeNode(3, nine, twenty)
    print(s.maxDepth(root))

if __name__ == '__main__':
    main()