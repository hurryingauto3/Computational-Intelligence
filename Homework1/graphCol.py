from EvolAlgo import EvolAlgo
import random as rd

class graphCol(EvolAlgo):
    
    def __init__(self, fileName, popSize = 100, numoffSpring = 10, numGen = 100, mutRate = 0.5, numIter = 100, selScheme = "fp", survivalSel = "fp"):
        EvolAlgo.__init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme, survivalSel) 
        x = lambda i: (int(i[1]), int(i[2]))
        self.nodes = [x(self.fileData[i].strip("\n").split(" ")) for i in range(1, len(self.fileData))]
        print(self.nodes)       

    def popInit(self): self.popInit = [[rd.randint(0, len(self.nodes)-1) for i in range(len(self.nodes))] for j in range(self.popSize)]
    # edit this function
    def compFitness(self, gene):

        uniqueColors = len(set(gene))
        #edge coloring violation
        edgeColoringViolation = 0
        for i in range(len(gene)-1):
            if gene[i] == gene[i+1]:
                edgeColoringViolation += 1
        return 1/(uniqueColors+edgeColoringViolation)

g = graphCol("gc-ds.txt", numGen = 10, selScheme="tr")  