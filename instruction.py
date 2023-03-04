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
            
        
        pass
    def __str__(self):
        result = "The Working Matrix is:\n"
        for each in self.workingMatrix:
            result += str(each) + "\n"
        result += "The binary matching matrix is: \n"
        for each in self.matchingMatrix:
            result += str(each) + "\n"
        return result
        pass
        
    pass


#testing is here
a = instructionGenerate();
print(a)