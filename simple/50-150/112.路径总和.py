# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        que = []
        que.append((root,root.val))
        while que:
            node, path = que.pop(0)
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                que.append((node.left,path+node.left.val))
            if node.right:
                que.append((node.right,path+node.right.val))
        return False
