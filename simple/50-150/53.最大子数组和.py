# 朴素算法，后看题解此应该为动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 暴力求解
        temp = nums[0]
        max_ = temp
        for i in range(1,len(nums)):
            if temp+nums[i] > nums[i]:
                # 当前序列加上此时元素的值大于nums[i]，说明最大序列可能出现在后续
                # 将temp看做一个求和之后的元素，若为负值则丢弃，从当前开始寻找
                temp+=nums[i]
                max_ = max(max_, temp)
            else:
                max_ = max(max_, nums[i])
                temp = nums[i]
        return max_

# 感谢作者@edelweisskoko   , 来源：力扣（LeetCode）   
  class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp_sum = 0
        res = nums[0]
        for num in nums:
            tmp_sum = max(tmp_sum + num, num)
            res = max(res, tmp_sum)
        return res

      
# 贪心算法
# 感谢作者:一起学计算机（leetcode）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = float('-inf')
        sum = 0
        n = len(nums)
        for i in range(n):
            sum+=nums[i]
            max_ = max(max_,sum)
            if sum < 0:
                sum = 0
        return max_
      
# 分治法：线段树
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        class wtevTree: #线段树
            lSum = 0
            rSum = 0
            iSum = 0
            mSum = 0
            def __init__(self,l,r,i,m):
                self.lSum = l
                self.rSum = r
                self.iSum = i
                self.mSum = m
            
        def pushUp(self, leftT:wtevTree, rightT:wtevTree) -> wtevTree:
            l = max(leftT.lSum, leftT.iSum+rightT.lSum)
            r = max(rightT.rSum,rightT.iSum+leftT.rSum)
            i = leftT.iSum+rightT.iSum
            m = max(leftT.rSum+rightT.lSum,max(leftT.mSum,rightT.mSum))
            return wtevTree(l,r,i,m)

        # 递归建立和获取输入区间所有字段的结构
        def getInfo(self, nums:List[int], left:int, right:int)->wtevTree:
            if(left==right):
                return wtevTree(nums[left],nums[left],nums[left],nums[left])
            mid = (left+right)>>1   #右移一位＝除以二
            leftT = getInfo(self, nums, left, mid)
            rightT = getInfo(self, nums, mid+1, right)
            return pushUp(self, leftT, rightT)
        
        if (not nums or len(nums)<=0):
            return 0
        lens = len(nums)
        return getInfo(self,nums,0,lens-1).mSum
        
