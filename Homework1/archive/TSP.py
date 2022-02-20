from EvolAlgo import EvolAlgo
import math
import random as rd
import numpy as np

class TSP(EvolAlgo):

    def __init__(self, fileName, popSize = 100, numoffSpring = 10, numGen = 100, mutRate = 0.5, numIter = 100, selScheme = "fp"):
        EvolAlgo.__init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme)
        x = lambda i: (float(i[1]), float(i[2]))
        self.cities = [x(self.fileData[i].strip("\n").split(" ")) for i in range(7, len(self.fileData)-1)]

        print(len(self.cities))

    def popInit(self):
        for i in range(self.popSize): 
            self.pop.append(list(range(len(self.cities))))
            np.random.shuffle(self.pop[i])
    
    def crossover(self, prnts):
        offspringList = []
        while(len(offspringList) != self.numoffSpring):
            p1 = rd.choice(list(prnts.keys()))
            p2 = rd.choice(list(prnts.keys()))
            if p1== p2:
                continue
            else:
                randIndex1 = rd.randint(0, self.knapsackItemNum-1)
                randIndex2 = rd.randint(0, self.knapsackItemNum-1)
                child = []
                for i in range(self.knapsackItemNum):
                    randChoice = rd.choice([self.pop[p1][randIndex1], self.pop[p2][randIndex2]])
                    if randChoice in child:
                        continue
                    else:
                        child.append(randChoice)
                offspringList.append(child)
        self.pop.extend(offspringList)

    def compFitness(self, gene):
        tourLength = 0
        for i in range(len(gene)-1):
            tourLength += math.sqrt((gene[i][0]-gene[i+1][0])**2 + (gene[i][1]-gene[i+1][1])**2)
        return 1/tourLength        
            
ts = TSP("tsp-ds.tsp", numGen = 10, selScheme="tr")
ts.popInit()
