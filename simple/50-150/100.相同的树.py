# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def issame(P,Q):
            if P and Q:
                if P.val != Q.val:
                    return False
                return issame(P.left,Q.left) and issame(P.right,Q.right)
            else:
                if P == Q:
                    return True
                else:
                    return False
        return(issame(p,q))

      
# 使用定义的函数更加简洁      
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif p and q:
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
      
      
      
      
# 感谢作者@pandawakaka      
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preorder(root):
            if not root:
                return [None]
            else:
                return [root.val] +preorder(root.left)+preorder(root.right)
        return preorder(p)==preorder(q)

作者：pandawakaka
链接：https://leetcode-cn.com/problems/same-tree/solution/xiang-tong-de-shu-python3xian-xu-bian-li-by-pandaw/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。      
