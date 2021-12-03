class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        for i in range(len(s)):
            if s[i] == 'M':
                num+=1000
            elif s[i] == 'D':
                num+=500
            elif s[i] == 'C':
                if i+1<len(s) and (s[i+1] == 'D'or s[i+1]=='M'):
                    num-=100
                else:
                    num+=100
            elif s[i] == 'L':
                num+=50
            elif s[i] == 'X':
                if i+1<len(s) and (s[i+1] == 'L'or s[i+1]=='C'):
                    num-=10
                else:
                    num+=10
            elif s[i] == 'V':
                num+=5
            elif s[i] == 'I':
                if i+1 < len(s) and (s[i+1] == 'V' or s[i+1] == 'X'):
                    num-=1
                else:
                    num+=1
        return num

    
# 记录题解中以为作者较为清晰的哈希表写法
class Solution:
    def romanToInt(self, s: str) -> int:
        # 定义哈希表
        Roman2Int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Int = 0
        n = len(s)
        # 最后一个元素没有被遍历到，保证list索引不越界
        for index in range(n - 1):
            if Roman2Int[s[index]] < Roman2Int[s[index + 1]]:
                Int -= Roman2Int[s[index]]
            else:
                Int += Roman2Int[s[index]]

        return Int + Roman2Int[s[-1]]

作者：z1m
链接：https://leetcode-cn.com/problems/roman-to-integer/solution/qing-xi-tu-jie-python3-by-ml-zimingmeng/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
