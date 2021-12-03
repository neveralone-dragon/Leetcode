class Solution:
    def isValid(self, s: str) -> bool:
        # 构建hash表
        brackets_Hash_in = {'(':1,'[':2,'{':3}
        brackets_Hash_out = {')':-1,']':-2,'}':-3}
        # 栈结构，后进献出
        stack = []
        for bracket in s:
            if bracket in brackets_Hash_in.keys():
                stack.append(brackets_Hash_in[bracket])
            else:
                if stack == []:
                    # 此时已经没有元素与右括号匹配
                    return False
                else:
                    # 弹出最后一个元素并记录
                    now_bracket = stack.pop()
                    if now_bracket+brackets_Hash_out[bracket] != 0:
                        # 如果不相匹配
                        return False
        if stack == []:
            # 遍历完为空列表说明全部匹配
            return True
        return False

  # 解法2  
    # 作者:DaydayLeetcode
    if len(s)%2 != 0:
            return False
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('[]','').replace('()','').replace('{}','')
        return True if s == '' else False

# 解法3    
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
        return len(stack) == 1

作者：jyd
链接：https://leetcode-cn.com/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
