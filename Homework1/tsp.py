from evolalgo import *


class TSP(evolAlgo):
    def __init__(self, fileName, nPop, nOffSpring, nGen, rMutation, nIter, pSel, sSel, minimize):
        evolAlgo.__init__(self, fileName, nPop, nOffSpring,
                          nGen, rMutation, nIter, pSel, sSel, minimize)

        def x(i): return (float(i[0]), float(i[1]))
        self.cities = [x(self.fileData[i].strip("\n").split(" "))
                       for i in range(7, len(self.fileData)-1)]

    def popInit(self):
        for i in range(self.nPop):
            chromosome = rd.sample(self.cities, len(self.cities))
            self.population.append(Chromosome(
                i, chromosome, self.compFitness(chromosome)))

    def compFitness(self, gene):
        tourLen = 0
        for i in range(len(gene)-1):
            tourLen += np.sqrt((gene[i][0]-gene[i+1][0])
                               ** 2 + (gene[i][1]-gene[i+1][1])**2)
        return tourLen

    def crossover(self):
        offSpring = []

        while(len(offSpring) < self.nOffSpring):
            p1 = rd.choice(self.parents)
            p2 = rd.choice(self.parents)
            if p1 != p2:
                
                p1Genes = list(p1.genes[0:int(rd.random()*len(p1.genes))])
                p2Genes = [i for i in p2.genes if i not in p1Genes]
                p3Genes = list(p2.genes[0:int(rd.random()*len(p2.genes))])
                p4Genes = [i for i in p1.genes if i not in p3Genes]           

                chromosome = p1Genes + p2Genes
                offSpring.append(Chromosome(0, chromosome, self.compFitness(chromosome)))
                chromosome = p3Genes + p4Genes
                offSpring.append(Chromosome(0, chromosome, self.compFitness(chromosome)))
            else:
                continue
        self.mutation(offSpring)
        for i in range(len(offSpring)):
            offSpring[i].id = self.nPop + i
        self.population.extend(offSpring)



