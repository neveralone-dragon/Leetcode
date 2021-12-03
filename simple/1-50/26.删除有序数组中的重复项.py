class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            # 当nums为空列表
            return 0
        fast = slow = 1
        while fast < len(nums):
            if nums[fast-1] < nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

