class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        yanghui_list = []
        for i in range(rowIndex+1):
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
        return yanghui_list[-1]
