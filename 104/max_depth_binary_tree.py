# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return Solution.dfs_depth(root, 0)

    @staticmethod
    def dfs_depth(root, depth):
        if (root == None):
            return depth

        return max(Solution.dfs_depth(root.left, depth + 1), Solution.dfs_depth(root.right, depth + 1))
