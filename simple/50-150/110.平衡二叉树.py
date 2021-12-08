# 定义求书深度的函数和判断是否平衡二叉树的函数                                        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def max_dep(root):
            if not root:
                return 0
            return 1 + max(max_dep(root.left),max_dep(root.right))
        def is_balance(root):
            if not root:
                return True
            return abs(max_dep(root.left)-max_dep(root.right)) <= 1 and is_balance(root.left) and is_balance(root.right)
        return is_balance(root)


# 感谢作者jyd
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1

    def recur(self, root):
        if not root: return 0
        left = self.recur(root.left)
        if left == -1: return -1
        right = self.recur(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

作者：jyd
链接：https://leetcode-cn.com/problems/balanced-binary-tree/solution/balanced-binary-tree-di-gui-fang-fa-by-jin40789108/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。        
