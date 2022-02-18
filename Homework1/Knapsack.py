from EvolAlgo import EvolAlgo
import numpy as np
import random as rd
from numpy.random import shuffle
class Knapsack(EvolAlgo):

    def __init__(self, fileName, popSize = 30, numoffSpring = 10, numGen = 100, mutRate = 0.5, numIter = 100, selScheme = "fp", survivalSel = "fp"):
        EvolAlgo.__init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme, survivalSel)
        x = lambda i: (int(i[0]), int(i[1]))
        self.knapsackItems = [x(self.fileData[i].strip("\n").split(" ")) for i in range(len(self.fileData))] #knapsack items
        self.knapsackItemNum = int(self.knapsackItems[0][0])  # Number of items
        self.knapsackCapacity = int(self.knapsackItems[0][1]) #knapsack capacity
        self.knapsackItems.pop(0)
        
    def popInit(self): self.pop = [np.random.randint(2, size = self.knapsackItemNum) for i in range(self.popSize)]

    def crossover(self):
        offspringList = []
        while(len(offspringList) != self.numoffSpring):
            p1 = rd.choice(list(self.parents.keys()))
            p2 = rd.choice(list(self.parents.keys()))
            if p1== p2:
                continue
            else:
                offspringList.append(self.pop[p1][0:self.knapsackItemNum//2] + self.pop[p2][self.knapsackItemNum//2:])
        #         randIndex1 = rd.randint(0, self.knapsackItemNum-1)
        #         randIndex2 = rd.randint(0, self.knapsackItemNum-1)
        #         offspringList.append([rd.choice([self.pop[p1][randIndex1], self.pop[p2][randIndex2]]) for i in range(self.knapsackItemNum)])
        self.mutation(offspringList)
        self.pop.extend(offspringList)
        
    def compFitness(self, gene):
        Sum_KW = sum([self.knapsackItems[i][0]*gene[i] for i in range(len(gene))])
        if Sum_KW > self.knapsackCapacity or Sum_KW <= 0:
            return 0
        Sum_KV = sum([self.knapsackItems[i][1]*gene[i] for i in range(len(gene))])
        #Needs to maxiumum
        return Sum_KV
    



ks = Knapsack("f2_l-d_kp_20_878", numGen = 100, numIter = 40, mutRate = 0.4, selScheme="tr", survivalSel="tr")
ks.run()
ks.plot()