# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildtree(low,high):
            if low > high:
                return None
            mid = (low+high)//2
            root = TreeNode(nums[mid])
            root.left = buildtree(low,mid-1)
            root.right = buildtree(mid+1,high)
            return root
        return buildtree(0,len(nums)-1)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            m = len(nums) // 2
            r = TreeNode(nums[m])
            r.left, r.right = map(self.sortedArrayToBST, [nums[:m], nums[m+1:]])
            return r

# 作者：QQqun902025048
# 链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/5-xing-python-di-gui-by-qqqun902025048/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
