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
        
    ## Popfitness storing popoulation fitness and popoulation as dictionary of touples
    def popInit(self): 
        for i in range(self.popSize):
            chromosome = np.random.randint(2, size = self.knapsackItemNum)
            self.popFitness[i] = (self.compFitness(chromosome), chromosome)
        
    def crossover(self):
        offspringList = []
        while(len(offspringList) != self.numoffSpring):
            p1 = rd.choice(list(self.parents.keys()))
            p2 = rd.choice(list(self.parents.keys()))
            if p1== p2:
                continue
            else:
                childp1 = self.popFitness[p1][1][0:self.knapsackItemNum//2]
                childp2 = self.popFitness[p1][1][self.knapsackItemNum//2:]
                offspringList.append(list(childp1)+list(childp2))
        
        offspringList = self.mutation(offspringList)
        
        j = 0
        for i in range(self.popSize, self.popSize+self.numoffSpring):
            self.popFitness[i] = (self.compFitness(offspringList[j]), offspringList[j])
            j+=1
        


    def compFitness(self, chrmsme):
        Sum_KW = sum([self.knapsackItems[i][0]*chrmsme[i] for i in range(len(chrmsme))])
        if Sum_KW > self.knapsackCapacity or Sum_KW <= 0:
            return 0
        Sum_KV = sum([self.knapsackItems[i][1]*chrmsme[i] for i in range(len(chrmsme))])
        #Needs to maxiumum
        return Sum_KV
    



ks = Knapsack("f2_l-d_kp_20_878", numGen = 10, numIter=1, mutRate = 0.4, selScheme="tr", survivalSel="tr")
ks.run()
ks.plot()