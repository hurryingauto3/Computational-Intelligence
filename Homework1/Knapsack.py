from EvolAlgo import EvolAlgo

#20 items and knapsack capacity is 878
class Knapsack(EvolAlgo):

    def __init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme):
        EvolAlgo.__init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme)

        [i.strip("\n") for i in self.fileData]
        [i.split(" ") for i in self.fileData]

        self.knapsackItemNum = self.fileData[0][0]  # Number of items
        self.knapsackCapacity = self.fileData[0][1] #knapsack capacity
        self.fileData.pop(0)
        self.knapsackItems = {}
        [knapsackItems[i] = fileData[i] for i range(self.knapsackItemNum)]
        
        print(self.knapsackItems)
    
    def popInit(self):
        return super().popInit()
    
    # def compFitness(self)

    def compFitnessAll(self):
        return super().compFitnessAll()
    
    def selScheme(self):
        return super().selScheme()

    def crossover(self):
        return super().crossover()
    
    def mutation(self):
        return super().mutation()

    # edit this function



ks = Knapsack("f2_l-d_kp_20_878", 100, 10, 100, 0.1, 100, "fp")
