from evolalgo import *


class graphcoloring(evolAlgo):
    def __init__(self, fileName, nPop, nOffSpring, nGen, rMutation, nIter, pSel, sSel):
        evolAlgo.__init__(self, fileName, nPop, nOffSpring,
                          nGen, rMutation, nIter, pSel, sSel)

        def x(i): return (int(i[1]), int(i[2]))
        self.edges = [x(self.fileData[i].strip("\n").split(" "))
                      for i in range(1, len(self.fileData))]
        self.nodes = list(set(i for j in self.edges for i in j))

    def popInit(self):
        for i in range(self.nPop):
            chromosome = [rd.randint(0, len(self.nodes)-1)
                          for i in range(len(self.edges))]
            self.population.append(Chromosome(
                i, chromosome, self.compFitness(chromosome)))

    def compFitness(self, gene):
        nonuniqueColors = len(self.nodes) - len(set(gene))
        # edge coloring violation
        edgeColoringViolation = 0
        for i in range(len(gene)-1):
            if gene[i] == gene[i+1]:
                edgeColoringViolation += 1
        return 1/(nonuniqueColors+edgeColoringViolation)

    def crossover(self):
        offSpring = []

        while(len(offSpring) < self.nOffSpring):
            p1 = rd.choice(self.parents)
            p2 = rd.choice(self.parents)
            if p1 != p2:
                p1Genes = list(p1.genes[0:int(len(p1.genes)/2)])
                p2Genes = list(p2.genes[int(len(p2.genes)/2):len(p2.genes)])
                chromosome = p1Genes + p2Genes
                offSpring.append(Chromosome(
                    0, chromosome, self.compFitness(chromosome)))
            else:
                continue
        self.mutation(offSpring)
        for i in range(len(offSpring)):
            offSpring[i].id = self.nPop + i
        self.population.extend(offSpring)


gs = graphcoloring("gc-ds.txt", 100, 20, 100, 0.1, 40, "tr", "tr")
gs.run()
gs.plot()
