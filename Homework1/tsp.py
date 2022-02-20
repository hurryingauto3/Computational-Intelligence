from evolalgo import *

class TSP(evolAlgo):
    def __init__(self, fileName, nPop, nOffSpring, nGen, rMutation, nIter, pSel, sSel):
        evolAlgo.__init__(self, fileName, nPop, nOffSpring, nGen, rMutation, nIter, pSel, sSel)
        x = lambda i: (int(i[0]), int(i[1]))
        self.cities = [x(self.fileData[i].strip("\n").split(" ")) for i in range(len(self.fileData))]


    def popInit(self):
        for i in range(self.nPop):
            chromosome = rd.sample(self.cities, len(self.cities))
            self.population.append(Chromosome(i, chromosome, self.compFitness(chromosome)))
    
    def compFitness(self, gene):
        tourLen = 0
        for i in range(len(gene)-1):
            tourLen += np.sqrt((gene[i][0]-gene[i+1][0])**2 + (gene[i][1]-gene[i+1][1])**2)