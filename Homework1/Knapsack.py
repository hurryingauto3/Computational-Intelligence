from EvolAlgo import EvolAlgo

class Knapsack(EvolAlgo):

    def __init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme):
        EvolAlgo.__init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme)  
        print(self.fileData)
    
    def popInit(self):
        return super().popInit()
    
    def compFitnessAll(self):
        return super().compFitnessAll()
    
    def selScheme(self):
        return super().selScheme()

    def crossover(self):
        return super().crossover()
    
    def mutation(self):
        return super().mutation()

    # edit this function
    def compFitness(self):
        return super().compFitness()


ks = Knapsack("f2_l-d_kp_20_878", 100, 10, 100, 0.1, 100, "fp")
