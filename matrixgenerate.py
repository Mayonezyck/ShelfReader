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
            self.generating(desiredBookArray,actualBookArray)
        print(self.result)
    
    def A_Match_D(a,b,c):
        return min(a,b,c)+0

    def A_notMatch_D(a,b,c):
        return min(a,b,c)+1
    
    def generating(self,desiredBookArray,actualBookArray):
        d_length = len(desiredBookArray)
        a_length = len(actualBookArray)
        for i_dBook in range(1,d_length+1):
            for i_aBook in range(1,a_length+1):
                if actualBookArray[i_aBook] == desiredBookArray[i_dBook]:
                    self.result[i_dBook][i_aBook].append(self.A_Match_D(self.result[i_dBook-1][i_aBook-1],self.result[i_dBook][i_aBook-1],self.result[i_dBook-1][i_aBook]))
                else:
                    self.result[i_dBook][i_aBook].append(self.A_notMatch_D(self.result[i_dBook-1][i_aBook-1],self.result[i_dBook][i_aBook-1],self.result[i_dBook-1][i_aBook]))
        print(self.result)

        #                ' ',1,2,3,4,5,6]        i_dBook = 1 -> 1
        #  self.    ' '  [0,1,2,3,4,5,6,7]    
        #            1   [1,"0,1,2,3,4,5,6]      i_aBook = 1 
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