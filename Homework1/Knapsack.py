from EvolAlgo import EvolAlgo
import numpy as np
class Knapsack(EvolAlgo):

    def __init__(self, fileName = "f2_l-d_kp_20_878", popSize = 100, numoffSpring = 10, numGen = 100, mutRate = 0.5, numIter = 100, selScheme = "fp"):
        EvolAlgo.__init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme)
        x = lambda i: (int(i[0]), int(i[1]))
        self.knapsackItems = [x(self.fileData[i].strip("\n").split(" ")) for i in range(len(self.fileData))] #knapsack items
        self.knapsackItemNum = int(self.knapsackItems[0][0])  # Number of items
        self.knapsackCapacity = int(self.knapsackItems[0][1]) #knapsack capacity
        self.knapsackItems.pop(0)
        
    def popInit(self):
        self.pop = [np.random.randint(2, size = self.knapsackItemNum) for i in range(self.popSize)]
        
    def compFitness(self, gene):
      
        Sum_KW = sum([self.knapsackItems[i][0]*gene[i] for i in range(len(gene))])
        if Sum_KW > self.knapsackCapacity:
            return 0
        Sum_KV = sum([self.knapsackItems[i][1]*gene[i] for i in range(len(gene))])
        return Sum_KV*Sum_KW

    def crossover(self):
        return super().crossover()
    
    def mutation(self):
        return super().mutation()





# ks = Knapsack(selScheme="tr")
# ks.popInit()
# ks.compFitnessAll()

# print(ks.bestFitness())
# print(ks.avgFitness())
# print(ks.popFitness)
# ks.schemeSel()
