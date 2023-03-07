#generate instruction based on matrix input
#Two matrices should be taken in. one is the Levenshtein matrix for the twenty books
#The other is a binary matrix that indicates the matching pairs of the Levenshtein matrix
#The output is supposed to be a list of strings, that the student should complete in order.
#
class instructionGenerate:
    def __init__(self) -> None:
        self.workingMatrix = [
            [0,1,2,3,4,5,6],[1,0,1,2,3,4,5],[2,1,1,1,2,3,4],
            [3,2,2,2,2,2,3],[4,3,3,3,2,3,3],[5,4,4,4,3,3,4],
            [6,5,4,5,4,4,4],[7,6,5,5,5,5,4]
            ]
        
        self.matchingMatrix = [
            [1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],
            [0,0,0,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0],[0,0,0,0,0,0,1]
            ]
        self.posx, self.posy = self.getSize()

    def __str__(self):
        result = "The Working Matrix is:\n"
        for each in self.workingMatrix:
            result += str(each) + "\n"
        result += "The binary matching matrix is: \n"
        for each in self.matchingMatrix:
            result += str(each) + "\n"
        return result
        

    def printMinSteps(self):
        print("It takes at least " + str(self.workingMatrix[-1][-1]) + " steps to reorder")

    def checkXY(self):
        return not( self.posx == 0 and self.posy == 0) 
    def printXY(self):
        print("The " + str(self.posx) +" and " + str(self.posy) + " were reached\n\tValue: " + str(self.workingMatrix[self.posx][self.posy]))
        #return posx, posy
    def traceBack(self, posx, posy):
        if(posx == 0 and posy == 0):
            print("Debug: The top left node was reached")
            return -1, -1
        elif(posx == 0 and posy != 0):
            return posx, posy-1
        elif(posx != 0 and posy == 0):
            return posx-1, posy
        else:
            if(self.workingMatrix[posx-1][posy-1] == self.workingMatrix[posx][posy]-1): return posx-1,posy-1
            else:
                left = self.workingMatrix[posx][posy-1]
                top = self.workingMatrix[posx-1][posy]
                topleft = self.workingMatrix[posx-1][posy-1]
                if left < top and left < topleft:
                    return posx, posy-1
                elif left > top and top < topleft:
                    return posx-1, posy
                else:
                    return posx-1, posy-1
    def getSize(self):
        return len(self.workingMatrix)-1 , len(self.workingMatrix[0])-1
    def traceBackOnce(self):
        self.posx, self.posy = self.traceBack(self.posx,self.posy)

#testing is here
a = instructionGenerate();
print(a)
a.printMinSteps()
print('')
a.printXY()
while(a.checkXY()):
    a.traceBackOnce()
    a.printXY()