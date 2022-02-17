from EvolAlgo import EvolAlgo
import numpy as np
import random as rd
from numpy.random import shuffle
class Knapsack(EvolAlgo):

    def __init__(self, fileName, popSize = 100, numoffSpring = 10, numGen = 100, mutRate = 0.5, numIter = 100, selScheme = "fp"):
        EvolAlgo.__init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme)
        x = lambda i: (int(i[0]), int(i[1]))
        self.knapsackItems = [x(self.fileData[i].strip("\n").split(" ")) for i in range(len(self.fileData))] #knapsack items
        self.knapsackItemNum = int(self.knapsackItems[0][0])  # Number of items
        self.knapsackCapacity = int(self.knapsackItems[0][1]) #knapsack capacity
        self.knapsackItems.pop(0)
        
    def popInit(self): self.pop = [np.random.randint(2, size = self.knapsackItemNum) for i in range(self.popSize)]
        
    def compFitness(self, gene):
        Sum_KW = sum([self.knapsackItems[i][0]*gene[i] for i in range(len(gene))])
        if Sum_KW > self.knapsackCapacity:
            return 0
        Sum_KV = sum([self.knapsackItems[i][1]*gene[i] for i in range(len(gene))])
        return (Sum_KV*(1/Sum_KW))*(1/np.sqrt(Sum_KV*(1/Sum_KW)))

    
        self.pop.extend(offspringList)



ks = Knapsack("f2_l-d_kp_20_878", numGen = 10, selScheme="rb")
ks.run()
