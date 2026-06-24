# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left) 
        self.flatten(root.right)
        if not root.left:
            return

        orginal_right = root.right
        
        temp = root.left
        root.right =  temp
        root.left = None
        curr = temp
        while curr and curr.right:
            curr = curr.right
        if curr:
            curr.right = orginal_right
      

        