# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        queue = deque()
        queue.append((root, 0))
        ans = 0
        while queue:
            n = len(queue)
            for i in range(n):
                node, idx = queue.popleft()
                if i == 0:
                   first = idx
                if i == n - 1:
                    last = idx
                if node.left:
                    queue.append((node.left, 2 * idx+ 1))
                if node.right:
                    queue.append((node.right, 2 * idx + 2))
                width = last - first + 1
                ans = max(ans, width)
        return ans