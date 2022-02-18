from EvolAlgo import EvolAlgo

class graphCol(EvolAlgo):
    
    def __init__(self, fileName, popSize = 100, numoffSpring = 10, numGen = 100, mutRate = 0.5, numIter = 100, selScheme = "fp", survivalSel = "fp"):
        EvolAlgo.__init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme, survivalSel) 
        x = lambda i: (int(i[1]), int(i[2]))
        self.nodes = [x(self.fileData[i].strip("\n").split(" ")) for i in range(1, len(self.fileData))]
        print(self.nodes)       

    def popInit(self):
        return super().popInit()

    # edit this function
    def compFitness(self):
        return super().compFitness()


g = graphCol("gc-ds.txt", numGen = 10, selScheme="tr")  