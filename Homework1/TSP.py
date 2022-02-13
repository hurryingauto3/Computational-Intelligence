from EvolAlgo import EvolAlgo

class TSP(EvolAlgo):

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
