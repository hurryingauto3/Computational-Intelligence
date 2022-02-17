# Class of generic evolutionary algorithm
from logging import error
import random as rd
import numpy as np

class SelectionScheme:
    @staticmethod

    def fitnessProp(N, fitness):
        fitnessSum = sum(fitness.values())
        fitnessProb = [i/fitnessSum for i in fitness.values()]
        return dict([(i, fitness[i]) for i in rd.choices(list(fitness.keys()), weights = fitnessProb, k = N)])

    def rankBased(N, fitness):
      pass

    def binaryTournament(k, pop):   
        '''Lets say your generation has 1000 individuals. You can now create 1000 
        new individuals for the next generation by having multiple tournaments of 
        size 2 where you pick the better individual out of 2 randomly chosen as a parent 
        for the next generation. Here k would be 2 and you'd run 2000 tournaments if 
        you're having just 1 parent per individual'''

        pass

    def truncation(N, fitness):
        popFitness = [(k,v) for k,v in fitness.items()]
        popFitness = popFitness[0:N]
        popFitness = dict(popFitness)
        return popFitness
        
    def random(N, fitness):

         return dict([(i, fitness[i]) for i in rd.choices(list(fitness.keys()), k = N)])

class EvolAlgo:
    @staticmethod
    def __init__(self, fileName, popSize = 100, numoffSpring = 10, numGen = 100, mutRate = 0.5, numIter = 100, selScheme = "fp"):

        self.fileData = self.readFile(fileName)
        self.selScheme = selScheme
        self.popSize = popSize
        self.numoffSpring = numoffSpring
        self.numGen = numGen
        self.mutRate = mutRate
        self.numIter = numIter
        self.popFitness = {}
        self.pop = []

    def readFile(self, fileName):

        f = open(fileName, "r")
        lines = f.readlines()
        f.close()
        return lines
    
    def crossover(self):
        pass

    def mutation(self):
        pass

    def popInit(self):
        pass
   
    def schemeSel(self, kill=False):
        if kill:
            N = self.popSize
        else:
            N = self.numoffSpring*2

        if self.selScheme == "fp":
            return SelectionScheme.fitnessProp(N, self.popFitness)
        elif self.selScheme == "rb":
            return SelectionScheme.rankBased(N, self.sortFitness())
        elif self.selScheme == "bt":
            return SelectionScheme.binaryTournament()
        elif self.selScheme == "tr":
            return SelectionScheme.truncation(N, self.sortFitness())
        elif self.selScheme == "rd":
            return SelectionScheme.random(N, self.sortFitness())
        else:
            error("Invalid selection scheme")
        pass

    def compFitnessAll(self):
        for i in range(self.popSize):
            self.popFitness[i] = self.compFitness(self.pop[i])
    def bestFitness(self):
        return max(self.popFitness.values())
    def avgFitness(self):
        return sum(self.popFitness.values())/self.popSize
    def sortFitness(self):
        return {k:v for k,v in sorted(self.popFitness.items(), key=lambda x: x[1])}

    def crossover(self, prnts):
        offspring = 0
        offspringList = []
        while(offspring != self.numoffSpring):
            p1 = rd.choice(list(prnts.keys()))
            p2 = rd.choice(list(prnts.keys()))
            if p1== p2:
                continue
            else:
                # child = rd.sample(list(prnts[p1]), self.knapsackItemNum//2) + rd.sample(list(prnts[p2]), self.knapsackItemNum - self.knapsackItemNum//2)
                child = self.pop[p1][0:self.knapsackItemNum//2] + self.pop[p2][self.knapsackItemNum//2::]
                offspringList.append(child)
                offspring += 1
    
    def mutation(self): 
        for i in range(len(self.pop)):
            if rd.random() < self.mutRate: np.random.shuffle(self.pop[i])

    def run(self):
        log = []
        for i in range(self.numIter):
            self.popInit()
            for j in range(self.numGen):
                self.compFitnessAll()
                # self.schemeSel()
                self.crossover(self.schemeSel())
                self.mutation()
                self.compFitnessAll()
                self.schemeSel(kill=True)
                log.append("Iteration: " + str(i+1) + ", " + "Generation: " + str(j+1) + ", " + "Best Fitness: " 
                + str(self.bestFitness()) + ", " + "Average Fitness: " + str(self.avgFitness()) + "\n")
        
        f = open("log.txt", "w")
        f.writelines(log)
        f.close()