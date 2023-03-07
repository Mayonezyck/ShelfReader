#matrixgenerate.py
#This class returns the matching matrix which will then be used in the instruction.py

class matrixgenerate:
    def __init__(self) -> None:
        self.result = [[0,1,2,3,4,5,6,7],[1,0,1,2,3,4,5,6],[2,1,1,2,2,3,4,5],[3,2,2,1,2,3,4,5],[4,3,3,2,2,3,3,4]
                              ,[5,4,3,3,3,3,4,5],[6,5,4,4,4,4,4,4],[7,6,5,5,5,4,5,5]]#TODO: figure out the matrix generating technique
    def getMatrix(self):
        return self.result