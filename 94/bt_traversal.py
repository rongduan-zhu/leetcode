# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        popped = False
        output = []
        stack = [root]

        while len(stack) > 0:
            if not popped and stack[-1].left != None:
                stack.append(stack[-1].left)
                continue

            if stack[-1].left == None or popped:
                node = stack.pop()
                popped = True
                output.append(node.val)

                if node.right != None:
                    stack.append(node.right)
                    popped = False

        return output
