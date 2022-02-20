from evolalgo import *


class graphcoloring(evolAlgo):
    def __init__(self, fileName, nPop, nOffSpring, nGen, rMutation, nIter, pSel, sSel):
        evolAlgo.__init__(self, fileName, nPop, nOffSpring, nGen, rMutation, nIter, pSel, sSel)
        x = lambda i: (int(i[1]), int(i[2]))
        self.edges = [x(self.fileData[i].strip("\n").split(" ")) for i in range(1, len(self.fileData))]
        self.nodes = list(set(i for j in self.edges for i in j))
    
    def popInit(self): 
        for i in range(self.nPop):
            chromosome = [rd.randint(0, len(self.nodes)-1) for i in range(len(self.edges))]
            self.population.append(Chromosome(i, chromosome, self.compFitness(chromosome)))
    
    def compFitness(self, gene):
        nonuniqueColors = 100 - len(set(gene))
        #edge coloring violation
        edgeColoringViolation = 0
        for i in range(len(gene)-1):
            if gene[i] == gene[i+1]:
                edgeColoringViolation += 1
        return 1/(nonuniqueColors+edgeColoringViolation)

