#test file
import matrixgenerate, instruction

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
for step in ig.solutionIndex:
    print(step + " replace with " + ig.solutionDictionary[step])
