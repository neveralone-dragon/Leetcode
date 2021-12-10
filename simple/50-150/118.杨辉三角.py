class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        yanghui_list = []
        for i in range(numRows):
            if i == 0:
                temp = [1]
            elif i == 1:
                temp = [1,1]
            else:
                temp = [1]
                for j in range(i-1):
                    temp.append(yanghui_list[-1][j]+yanghui_list[-1][j+1])
                temp.append(1)
            yanghui_list.append(temp)
        return yanghui_list
      
      
# 官方写的更为简洁

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/pascals-triangle/solution/yang-hui-san-jiao-by-leetcode-solution-lew9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
