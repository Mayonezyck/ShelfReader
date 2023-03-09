#matrixgenerate.py
#This class returns the matching matrix which will then be used in the instruction.py

class matrixgenerate:
    def __init__(self,desiredBookArray = None, actualBookArray = None) -> None:
        if desiredBookArray is None:
            self.result = [[0,1,2,3,4,5,6,7],[1,0,1,2,3,4,5,6],[2,1,1,2,2,3,4,5],[3,2,2,1,2,3,4,5],[4,3,3,2,2,3,3,4]
                              ,[5,4,3,3,3,3,4,5],[6,5,4,4,4,4,4,4],[7,6,5,5,5,4,5,5]]
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
    
    def A_Match_D(a,b,c,d):
        return min(a,b,c,d)+0

    def A_notMatch_D(a,b,c,d):
        return min(a,b,c,d)+1
    
    def generating(self):
        for index_d in range(1,len(self.desiredBookArray)+1):
            desired_book = self.desiredBookArray[index_d]
            for index_a in range(1,len(self.actualBookArray)+1):
                actual_book = self.actualBookArray[index_a]
                if desired_book == actual_book:
                    self.result.append(self.A_Match_D(index_d,desired_book,index_a,actual_book))
                else:
                    self.result.append(self.A_notMatch_D(index_d,desired_book,index_a,actual_book))
        print(self.result)

    def getMatrix(self):
        return self.result
    
db = [1,2,3,4,5,6]#desired book array
ab = [1,2,3,5,6,4,7]#actual book array
m = matrixgenerate(db, ab)