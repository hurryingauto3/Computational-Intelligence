from EvolAlgo import EvolAlgo
import numpy as np
from random import random, randint, choice
from numpy.random import shuffle
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
        return Sum_KV*(1/Sum_KW)

    def crossover(self, parents: dict()):
        offspring = 0
        offspringList = []
        while(offspring != self.numoffSpring):
            parent1 = choice(list(parents.keys()))
            parent2 = choice(list(parents.keys()))

            if parent1 == parent2:
                continue
            else:
                child = self.pop[parent1][0:self.knapsackItemNum//2] + self.pop[parent2][self.knapsackItemNum//2::]
                offspringList.append(child)
                offspring += 1

        self.pop.extend(offspringList)

    def mutation(self):
        for i in self.pop:
            shuffle(i)

ks = Knapsack(numGen=1, selScheme="tr")
ks.run()
# ks.popInit()
# ks.compFitnessAll()

# print(ks.bestFitness())
# print(ks.avgFitness())
# print(len(ks.pop))
# ks.crossover(ks.schemeSel())
# print(len(ks.pop))
