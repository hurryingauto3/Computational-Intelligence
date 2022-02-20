from evolalgo import *


class knapsack(evolAlgo):

    def __init__(self, fileName, nPop, nOffSpring, nGen, rMutation, nIter, pSel, sSel):
        evolAlgo.__init__(self, fileName, nPop, nOffSpring,
                          nGen, rMutation, nIter, pSel, sSel)

        def x(i): return (int(i[0]), int(i[1]))
        self.knapsackItems = [x(self.fileData[i].strip("\n").split(
            " ")) for i in range(len(self.fileData))]  # knapsack items
        self.knapsackItemNum = int(self.knapsackItems[0][0])  # Number of items
        self.knapsackCapacity = int(
            self.knapsackItems[0][1])  # knapsack capacity
        self.knapsackItems.pop(0)

    def popInit(self):
        for i in range(self.nPop):
            chomosome = np.random.randint(2, size=self.knapsackItemNum)
            self.population.append(Chromosome(
                i, chomosome, self.compFitness(chomosome)))

    def compFitness(self, chromosome):
        Sum_KW = sum([self.knapsackItems[i][0]*chromosome[i]
                     for i in range(len(chromosome))])
        if Sum_KW > self.knapsackCapacity or Sum_KW <= 0:
            return 0
        Sum_KV = sum([self.knapsackItems[i][1]*chromosome[i]
                     for i in range(len(chromosome))])
        # Needs to maxiumum
        return Sum_KV*(1/Sum_KW)

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


ks = knapsack("f2_l-d_kp_20_878", 30, 10, 20, 0.4, 40, "tr", "tr")
ks.run()
ks.plot("Total Value/Total Weight","knapsack")
# ks.popInit()
# print(len(ks.population))
# ks.parentSelection()
# ks.crossover()
# print(len(ks.population))
# ks.compFitnessAll()
# ks.survivalSelection()
# ks.population = ks.survivors
# print(len(ks.population))
