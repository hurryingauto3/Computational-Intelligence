from evolalgo import *

class knapsack(evolAlgo):

    def __init__(self, fileName, nPop, nOffSpring, nGen, rMutation, nIter, pSel, sSel):
        evolAlgo.__init__(self, fileName, nPop, nOffSpring, nGen, rMutation, nIter, pSel, sSel)
        x = lambda i: (int(i[0]), int(i[1]))
        self.knapsackItems = [x(self.fileData[i].strip("\n").split(" ")) for i in range(len(self.fileData))] #knapsack items
        self.knapsackItemNum = int(self.knapsackItems[0][0])  # Number of items
        self.knapsackCapacity = int(self.knapsackItems[0][1]) #knapsack capacity
        self.knapsackItems.pop(0)
 
    def popInit(self):
        for i in range(self.popSize):
            chomosome = np.random.randint(2, size = self.knapsackItemNum)
            self.population.append(Chromosome(i, chomosome, self.compFitness(chomosome)))
    
    def compFitness(self, chromosome):
        Sum_KW = sum([self.knapsackItems[i][0]*chromosome[i] for i in range(len(chromosome))])
        if Sum_KW > self.knapsackCapacity or Sum_KW <= 0:
            return 0
        Sum_KV = sum([self.knapsackItems[i][1]*chromosome[i] for i in range(len(chromosome))])
        #Needs to maxiumum
        return Sum_KV
    
