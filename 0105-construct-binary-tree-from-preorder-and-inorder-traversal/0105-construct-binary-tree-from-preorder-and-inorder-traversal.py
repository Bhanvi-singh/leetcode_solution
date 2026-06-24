# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not preorder:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        left_inorder = inorder[:idx]
        right_inorder = inorder[idx + 1:]
        len_size = len(left_inorder)
        left_preorder = preorder[1 : len_size + 1]
        right_preorder = preorder[len_size + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder) 
        return root