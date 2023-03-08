#matrixgenerate.py
#This class returns the matching matrix which will then be used in the instruction.py

class matrixgenerate:
    def __init__(self,desiredBookArray = None, actualBookArray = None) -> None:
        if desiredBookArray is None:
            self.result = [[0,1,2,3,4,5,6,7],[1,0,1,2,3,4,5,6],[2,1,1,2,2,3,4,5],[3,2,2,1,2,3,4,5],[4,3,3,2,2,3,3,4]
                              ,[5,4,3,3,3,3,4,5],[6,5,4,4,4,4,4,4],[7,6,5,5,5,4,5,5]]
        else:    
            self.result = []
            for i in range(len(actualBookArray)+1):
                self.result.append([])
            for i in range(len(desiredBookArray)+1):
                self.result[0].append(i)
        print(self.result)
        #TODO: figure out the matrix generating technique
    
    def getMatrix(self):
        return self.result
    
db = [1,2,3,4,5,6]
ab = [1,2,3,5,6,4,7]
m = matrixgenerate(db, ab)
