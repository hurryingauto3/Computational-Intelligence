from evolalgo import *


class knapsack(evolAlgo):

    def __init__(self, fileName, nPop, nOffSpring, nGen, rMutation, nIter, pSel, sSel, minmize):
        evolAlgo.__init__(self, fileName, nPop, nOffSpring,
                          nGen, rMutation, nIter, pSel, sSel, minmize)

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
        return Sum_KV

ks = knapsack("f2_l-d_kp_20_878", 30, 10, 500, 0.2, 40, "tr", "tr", False)
ks.run()
ks.plot("Total Value","knapsack")

