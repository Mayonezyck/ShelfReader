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
        #print(self.result)
        #TODO: figure out the matrix generating technique
    
    def A_Match_D(a,b,c):
        return min(a,b,c,d)+0

    def A_notMatch_D(a,b,c,d):
        return min(a,b,c,d)+1
    
    def generating(self):
        d_length = len(self.desiredBookArray)
        a_length = len(self.actualBookArray)
        for i_dBook in range(1,d_length+1):
            for i_aBook in self.actualBookArray:
                if self.actualBookArray[i_aBook] == self.desiredBookArray[i_dBook]:
                    self.result[i_dBook].append(self.A_Match_D(self.result[i_dBook-1][i_aBook-1],self.result[i_dBook][i_aBook-1],self.result[i_dBook-1][i_aBook]))
                else:
                    self.result[i_dBook].append(self.A_notMatch_D(self.result[i_dBook-1][i_aBook-1],self.result[i_dBook][i_aBook-1],self.result[i_dBook-1][i_aBook]))

            
        # for index_d in range(1,d_length+1):
        #     desired_book = self.desiredBookArray[index_d]
        #     for index_a in range(1,a_length+1):
        #         actual_book = self.actualBookArray[index_a]
        #         if desired_book == actual_book:
        #             self.result.append(self.A_Match_D(index_d,desired_book,index_a,actual_book))
        #         else:
        #             self.result.append(self.A_notMatch_D(index_d,desired_book,index_a,actual_book))
        # print(self.result)

        #                ' ',1,2,3,4,5,6]        i_dBook = 1 -> 1
        #  self.    ' '  [0,1,2,3,4,5,6,7],     
        #            1   [1,"0,1,2,3,4,5,6]      i_aBook = 1 
        #            2   [2,"1,1,2,3,4,5,5],
        #            3   [3,"2,1,2,3,4,5,6]
        #            5   [4,"3,2,1,2,3,4,5]
        #            6   [5,"4,3,2,1,2,3,4],
        #            4   [6,"5,4,3,2,1,2,3],
        #            7   [7,"6,5,4,3,2,1,2]]

    def getMatrix(self):
        return self.result
    
db = [1,2,3,4,5,6]#desired book array
ab = [1,2,3,5,6,4,7]#actual book array
m = matrixgenerate(db, ab)