# Class of generic evolutionary algorithm
from audioop import avg
import imp
from logging import error
import random as rd
from re import T
import numpy as np
import matplotlib.pyplot as plt

class Chromosome:
    def __init__(self, genes, fitness) -> None:
        self.genes = genes
        self.fitness = fitness
        self.parent = False
        self.survivor = True
        
class EvolAlgo:
    @staticmethod
    def __init__(self, fileName, popSize = 30, numoffSpring = 10, numGen = 100, mutRate = 0.5, numIter = 100, selScheme = "fp", survivalSel = "fp"):

        self.fileData = self.readFile(fileName)
        self.selScheme = selScheme
        self.survivalSel = survivalSel
        self.popSize = popSize
        self.numoffSpring = numoffSpring
        self.numGen = numGen
        self.mutRate = mutRate
        self.numIter = numIter
        self.population = {}
        self.parents = {}
        self.popFitness = {}
        self.bestFitnesses = []
        self.avgFitnesses = []
      
    def readFile(self, fileName):
        f = open(fileName, "r")
        lines = f.readlines()
        f.close()
        return lines
    
    def fitnessProp(N, fitness):
        fitnessSum = sum(fitness.values())
        fitnessProb = [i/fitnessSum for i in fitness.values()]
        return dict([(i, fitness[i]) for i in rd.choices(list(fitness.keys()), weights = fitnessProb, k = N)])

    def rankBased(N, fitness):
        pass

    def binaryTournament(N, fitness):   
        bestFitness = []
        while(len(bestFitness) < N):
            c1 = rd.choice(list(fitness.keys()))
            c2 = rd.choice(list(fitness.keys()))
            if fitness[c1] > fitness[c2]:
                if c1 in bestFitness:
                    continue
                bestFitness.append(c1)
            else:
                if c2 in bestFitness:
                    continue
        return dict([(i, fitness[i]) for i in bestFitness])


    def truncation(self, N, kill):
        popFitness = [i for i in self.popFitness.items()]
        if kill:
            print("All")
            print("Survived", [i[1][0] for i in popFitness[:N]])
            print("Killed", [i[1][0] for i in popFitness[N:]])
            return dict(popFitness[0:N])
        else:
            print("Parents", [i[1][0] for i in popFitness[:N]])
            print("NotP", [i[1][0] for i in popFitness[N:]])
            return dict(popFitness[0:N])

    def random(N, fitness):
         return dict([(i, fitness[i]) for i in rd.choices(list(fitness.keys()), k = N)])

    def schemeSel(self, kill=False):
        if kill:
            N = self.popSize
            if self.survivalSel == "fp":
                self.fitnessProp(N, self.popFitness)
            elif self.survivalSel == "rb":
                self.rankBased(N, self.sortFitness())
            elif self.survivalSel == "bt":
                self.binaryTournament(N, self.sortFitness())
            elif self.survivalSel == "tr":
                return self.truncation(N, kill)
            elif self.survivalSel == "rd":
                self.random(N, self.sortFitness())
            else:
                error("Invalid selection scheme")
        else:
            N = self.numoffSpring*2
            if self.selScheme == "fp":
                self.fitnessProp(N, self.popFitness)
            elif self.selScheme == "rb":
                self.rankBased(N, self.sortFitness())
            elif self.selScheme == "bt":
                self.binaryTournament(N, self.sortFitness())
            elif self.selScheme == "tr":
                return self.truncation(N, kill)
            elif self.selScheme == "rd":
                self.random(N, self.sortFitness())
            else:
                error("Invalid selection scheme")

    def compFitnessAll(self):
        for i in self.popFitness.keys():
            self.popFitness[i] = (self.compFitness(self.popFitness[i][1]), self.popFitness[i][1])
    
    def bestFitness(self): return max([self.popFitness[i][0] for i in self.popFitness.keys()])
    
    def avgFitness(self): return sum([self.popFitness[i][0] for i in self.popFitness.keys()])/self.popSize
    
    def sortFitness(self): 
        sortedFitness = sorted(self.popFitness.items(), key = lambda tup: tup[1][0], reverse=True)
        tempPopFitness = {}
        for i in sortedFitness:
            tempPopFitness[i[0]] = i[1]
        self.popFitness = tempPopFitness


    def mutation(self, offspringList): 
        for i in range(len(offspringList)):
            if rd.random() < self.mutRate: np.random.shuffle(offspringList[i])
        return offspringList

    def run(self):
        
        self.popInit()
        for j in range(self.numGen):
            #100 solutions
            bestFitness = 0
            avgFitness = 0
            for i in range(self.numIter):
                self.sortFitness()
                
                # print("Old gen", [self.popFitness[i][0]for i in self.popFitness.keys()])
                self.parents = self.schemeSel()
                self.crossover()
                self.sortFitness()
                # print("w/Offspring", [self.popFitness[i][0] for i in self.popFitness.keys()])
                self.compFitnessAll()
                self.sortFitness()
                self.popFitness = self.schemeSel(kill=True)
                # print("Survivors", [self.popFitness[i][0] for i in self.popFitness.keys()], "\n")

                bestFitness += self.bestFitness()
                avgFitness += self.avgFitness()
                # log.append("Iteration: " + str(i+1) + ", " + "Generation: " + str(j+1) + ", " + "Best Fitness: " 
                # + str(self.bestFitness()) + ", " + "Average Fitness: " + str(self.avgFitness()) + "\n")

            self.bestFitnesses.append(bestFitness/self.numIter)
            self.avgFitnesses.append(avgFitness/self.numIter)

    def plot(self):
        plt.plot(self.bestFitnesses)
        plt.plot(self.avgFitnesses)
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.legend(["Average Best Fitness over " + str(self.numIter), "Average Fitness over " + str(self.numIter)])
        plt.savefig("plot.png")
