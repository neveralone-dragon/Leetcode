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
                    return False
                else:
                    # 弹出最后一个元素并记录
                    now_bracket = stack.pop()
                    if now_bracket+brackets_Hash_out[bracket] != 0:
                        return False
        if stack == []:
            return True
        return False
