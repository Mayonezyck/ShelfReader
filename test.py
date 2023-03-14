#test file
import matrixgenerate, instruction

pseudoBookList = [None,"Book1", "Book2", "Book3", "Book4", "Book5", "Book6", "Book7"]#None acts as a padding component for empty string
pseudoShelfList = [None, "Book1", "Book7", "Book2", "Book3", "Book4", "Book5", "Book6"]#None acts as a padding component
mg = matrixgenerate.matrixgenerate()
matrix = mg.getMatrix()
ig = instruction.instructionGenerate(matrix)
print(ig)
ig.printMinSteps()
print('')
#print(a.solutionStepCount)
#a.printXY()
ig.tracBackToTop()
ig.flipSolutionIndex()
solutionDic, solutionInd = ig.getSolution()
print(solutionDic)
for step in solutionInd:
    shelfind = int(step)
    bookind = int(solutionDic[step])
    if(bookind == -1):
        print("Remove " + pseudoShelfList[shelfind])
    elif(bookind == -2):
        print("Add in " +pseudoBookList[shelfind]+ " after " + pseudoShelfList[shelfind])
    else:
        print(pseudoShelfList[shelfind] + " replace with " + pseudoBookList[bookind])

print(solutionInd)
#for step in solutionInd:
#    solutionInd.remove(step)
#bookInHand = pseudoShelfList[]



print(solutionInd)


