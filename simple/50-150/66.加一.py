# 写了个比较冗余的条件判定函数
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]+1 < 10:
            digits[-1] = digits[-1]+1
        else:
            i = -2
            digits[-1] = 0
            while abs(i) <= len(digits):
                if digits[i] + 1 == 10:
                    digits[i] = 0
                    i -= 1
                else:
                    digits[i] += 1
                    break
            if i == -len(digits)-1:
                digits.insert(0,1)
                digits[1] = 0
        return digits
      
 # 感谢leetcode@pi-pi-ch,思路一致，但是代码更加清晰，值得我学习
class Solution:
    def plusOne(self, digits: list) -> list:
        digits[-1]+=1  # 首先把最后一位加一
        for i in range(len(digits)-2,-1,-1):  # 从低位到高位遍历
            if digits[i+1]>=10:  # 如果低位>=10，那前一位的高位可以加一
                digits[i+1]=digits[i+1]%10
                digits[i]+=1
            else:  # 如果我们的在某一位的数字没有产生进位的话，那么之后的高位再也不可能进位了，直接跳出
                break


        if digits[0]>=10:  # 对最高位稍做处理，如解题思路中的[9,9,9]
            digits=[1]+digits
            digits[1]%=digits[1]

        return digits

# 作者：pi-pi-ch
# 链接：https://leetcode-cn.com/problems/plus-one/solution/gao-xiao-jie-fa-pythonfu-xiang-xi-zhu-sh-aw2e/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#感谢@zerolovecode
#代码非常的简洁，但是提升了复杂度
class Solution:
    def plusOne(self, digits):
        return [int(x) for x in list(str(int(''.join([str(i) for i in digits])) + 1))]

作者：zerolovecode
链接：https://leetcode-cn.com/problems/plus-one/solution/python3-yi-xing-jie-jue-by-zerolovecode-36v9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
