
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
            else:
                if i+1 == len(nums) or (i+1<len(nums) and nums[i+1]>target):
                    return i+1
            
# 二分法实现
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        long = len(nums)
        low = 0
        high = long - 1
        while low <= high:
            mid = (high + low )//2 
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return low
            

# 作者：inspiring-elbakyankvl
# 链接：https://leetcode-cn.com/problems/search-insert-position/solution/er-fen-fa-shi-xian-35-by-inspiring-elbak-htjn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
