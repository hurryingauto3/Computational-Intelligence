from evolalgo import *


class TSP(evolAlgo):
    def __init__(self, fileName, nPop, nOffSpring, nGen, rMutation, nIter, pSel, sSel, minimize):
        evolAlgo.__init__(self, fileName, nPop, nOffSpring,
                          nGen, rMutation, nIter, pSel, sSel, minimize)

        def x(i): return (int(i[0]), int(i[1]))
        self.cities = [x(self.fileData[i].strip("\n").split(" "))
                       for i in range(len(self.fileData))]

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
                p1Genes = list(p1.genes[0:int(len(p1.genes)//2)])
                p2Genes = list(p2.genes[int(len(p2.genes)//2):len(p2.genes)])
                p3Genes = list(p2.genes[0:int(len(p2.genes)//2)])
                p4Genes = list(p1.genes[int(len(p1.genes)//2):len(p1.genes)])
                for i in range(len(p1Genes)):
                    if p1Genes[i] in p2Genes:
                        p2Genes.replace(p1Genes[i], p2Genes[i])
                    if p2Genes[i] in p1Genes:
                        p1Genes.replace(p2Genes[i], p1Genes[i])
                    if p3Genes[i] in p4Genes:
                        p4Genes.replace(p3Genes[i], p4Genes[i])
                    if p4Genes[i] in p3Genes:
                        p3Genes.replace(p4Genes[i], p3Genes[i])
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


tsp = TSP("tsp-ds.tsp", 30, 10, 100, 0.5, 40, "tr", "tr", minimize=True)
tsp.run()
tsp.plot("Tour Length", "TSP")
