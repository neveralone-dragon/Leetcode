# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not (root.left or root.right):return 1
        elif not root.left:
            return self.minDepth(root.right)+1
        elif not root.right:
            return self.minDepth(root.left)+1
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))
        
        
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = deque()
        que.append(root)
        res = 1

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                # 当左右孩子都为空的时候，说明是最低点的一层了，退出
                if not node.left and not node.right:
                    return res
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            res += 1
        return res

作者：carlsun-2
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/dai-ma-sui-xiang-lu-dai-ni-xue-tou-er-ch-uq84/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。        
