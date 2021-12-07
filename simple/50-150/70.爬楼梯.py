# 递归调用+O(n)的数组存储
class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归求解子问题
        def sub_climb(sub_n:int, a:list):
            if sub_n == 1 or sub_n==0:
                return 1
            elif a[sub_n] == -1:
                a[sub_n] = sub_climb(sub_n-1,a)+sub_climb(sub_n-2,a)
            return a[sub_n]
        return sub_climb(n,[-1]*(n+1))
      
# 感谢作者@作者：lu-nan-2
# 自底向上
# 一维dp，自底向上，空间复杂度O(n)
def climbStairs(self, n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]

# 空间复杂度O(2)
# f(n)只依赖于f(n-1)和f(n-2)，只需要两项就足够了
def climbStairs(self, n: int) -> int:
    a = b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


# 作者：lu-nan-2
# 链接：https://leetcode-cn.com/problems/climbing-stairs/solution/zhi-xin-hua-shi-pa-lou-ti-zhi-cong-bao-l-lo1t/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
