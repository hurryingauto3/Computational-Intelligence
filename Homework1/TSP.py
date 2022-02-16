from EvolAlgo import EvolAlgo
from numpy.random import shuffle

class TSP(EvolAlgo):

    def __init__(self, fileName, popSize = 100, numoffSpring = 10, numGen = 100, mutRate = 0.5, numIter = 100, selScheme = "fp"):
        EvolAlgo.__init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme)
        x = lambda i: (float(i[1]), float(i[2]))
        self.cities = [x(self.fileData[i].strip("\n").split(" ")) for i in range(7, len(self.fileData)-1)]

        print(len(self.cities))
    def popInit(self):
        for i in range(self.popSize): 
            self.pop.append(list(range(len(self.cities))))
            shuffle(self.pop[i])
            
    # def compFitness(self, gene):
        
        




ts = TSP("tsp-ds.tsp", numGen = 10, selScheme="tr")
ts.popInit()
