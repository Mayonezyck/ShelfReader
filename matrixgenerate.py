#matrixgenerate.py
#This class returns the matching matrix which will then be used in the instruction.py

class matrixgenerate:
    def __init__(self,desiredBookArray = None, actualBookArray = None) -> None:
        if desiredBookArray is None:
            self.result = [[0,1,2,3,4,5,6,7],[1,0,1,2,3,4,5,6],[2,1,1,2,3,4,5,5],[3,2,1,2,3,4,5,6],[4,3,2,1,2,3,4,5]
                              ,[5,4,3,2,1,2,3,4],[6,5,4,3,2,1,2,3],[7,6,5,4,3,2,1,2]]
        else:    
            self.result = []
            temp = 0
            for i in range(len(actualBookArray)+1):
                self.result.append([temp])
                temp += 1
            for i in range(1,len(desiredBookArray)+1):
                self.result[0].append(i)
        print(self.result)
    
    def A_Match_D(self,a,b,c):
        return min(a,b,c) + 0

    def A_notMatch_D(self,a,b,c):
        return min(a,b,c) + 1
    
    def generating(self,desiredBookArray,actualBookArray):
        d_length = len(desiredBookArray)
        a_length = len(actualBookArray)
        row = 0
        for i_dBook in range(d_length+1):
            col = 0
            for i_aBook in range(a_length+1):   
                up_left = self.result[row][col]
                up_right = self.result[row][col+1]
                down_left = self.result[row+1][col]
                print(up_left, up_right, down_left)
                if actualBookArray[i_aBook] == desiredBookArray[i_dBook]:
                     no_action = self.A_Match_D(up_left,up_right,down_left)
                     self.result[col+1].append(no_action) 
                else:
                     do_oneStep = self.A_notMatch_D(up_left,up_right,down_left)
                     self.result[col+1].append(do_oneStep)
                col += 1
                #print(self.result[i_dBook][i_aBook])
                print(self.result)
            row += 1
        print(self.result)

        #                ' ',1,2,3,4,5,6]        i_dBook = 1 -> 1
        #  self.    ' '  [0,1,2,3,4,5,6,7]    
        #            1   [1,0,1,"2,3,4,5,6]      i_aBook = 1 
        #            2   [2,"1,1,2,3,4,5,5]
        #            3   [3,"2,1,2,3,4,5,6]
        #            5   [4,"3,2,1,2,3,4,5]
        #            6   [5,"4,3,2,1,2,3,4]
        #            4   [6,"5,4,3,2,1,2,3]
        #            7   [7,"6,5,4,3,2,1,2]]

    def getMatrix(self):
        return self.result
    
db = [1,2,3,4,5,6]#desired book array
ab = [1,2,3,5,6,4,7]#actual book array
m = matrixgenerate(db,ab)
m.generating(db,ab)