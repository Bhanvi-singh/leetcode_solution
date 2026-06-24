# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]].
        """
        if not root:
            return
        queue = deque()
        result = defaultdict(list)
        queue.append((root, 0, 0))
        while queue:
            node, line,level = queue.popleft()
            result[line].append((level, node.val))
            if node.left:
                queue.append((node.left, line - 1, level + 1)) 
            if node.right:
                queue.append((node.right, line +  1, level + 1))
        ans = []
        for line in sorted(result.keys()):
            temp = []
            for level, val in sorted(result[line]):
                temp.append(val)
            ans.append(temp)
        return ans

        