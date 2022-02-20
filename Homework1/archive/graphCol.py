from EvolAlgo import EvolAlgo
import random as rd

class graphCol(EvolAlgo):
    
    def __init__(self, fileName, popSize = 30, numoffSpring = 10, numGen = 40, mutRate = 0.5, numIter = 100, selScheme = "fp", survivalSel = "fp"):
        EvolAlgo.__init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme, survivalSel) 
        x = lambda i: (int(i[1]), int(i[2]))
        self.edges = [x(self.fileData[i].strip("\n").split(" ")) for i in range(1, len(self.fileData))]
        self.nodes = list(set(i for j in self.edges for i in j))
    
    def popInit(self): self.pop = [ for j in range(self.popSize)]
    # edit this function
    def compFitness(self, gene):

        nonuniqueColors = 100 - len(set(gene))
        #edge coloring violation
        edgeColoringViolation = 0
        for i in range(len(gene)-1):
            if gene[i] == gene[i+1]:
                edgeColoringViolation += 1
        return 1/(nonuniqueColors+edgeColoringViolation)
    
    def crossover(self, prnts):
        offspringList = []
        while(len(offspringList) != self.numoffSpring):
            p1 = rd.choice(list(prnts.keys()))
            p2 = rd.choice(list(prnts.keys()))
            if p1== p2:
                continue
            else:
                randIndex1 = rd.randint(0, len(self.edges)-1)
                randIndex2 = rd.randint(0, len(self.edges)-1)
                offspringList.append([rd.choice([self.pop[p1][randIndex1], self.pop[p2][randIndex2]]) for i in range(len(self.edges))])
        self.pop.extend(offspringList)

gs = graphCol("gc-ds.txt", popSize = 130, numoffSpring=60,numIter = 100, mutRate = 0.4, selScheme="tr", survivalSel="tr")
gs.run()
gs.plot()