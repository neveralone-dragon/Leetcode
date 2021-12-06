class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        for i in range(x//2+1):
            if x>=i*i and (i+1)*(i+1)>x:
                return i
             

#感谢@Dine
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x/2+1
        while l<=r:
            mid = (l+r)//2
            if mid > x/mid:
                r = mid - 1
            elif mid < x/mid:
                l = mid + 1
            else:
                return int(mid)
        return int(r)
