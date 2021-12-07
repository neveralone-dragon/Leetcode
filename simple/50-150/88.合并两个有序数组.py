# 直接合并后排序
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        nums1[m:] = nums2
        nums1.sort()

# 采用双指针
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        p1,p2 = 0,0
        while p1<m or p2<n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] <nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2+=1
        nums1[:] = sorted
        
        

# 作者：gu-xx-qi
# 链接：https://leetcode-cn.com/problems/merge-sorted-array/solution/si-wei-dao-tu-zheng-li-liang-chong-shuan-iahh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。        
