# Class of generic evolutionary algorithm
from logging import error
from nis import match
import random as rd
import numpy as np
import matplotlib.pyplot as plt


class Chromosome:
    def __init__(self, id, genes, fitness) -> None:
        self.id = id
        self.genes = genes
        self.fitness = fitness


class evolAlgo:
    @staticmethod
    def __init__(self, fileName, nPop, nOffSpring, nGen, rMutation, nIter, pSel, sSel):

        self.fileData = self.readFile(fileName)
        # Initialize parameters
        self.nPop = nPop
        self.nOffSpring = nOffSpring
        self.nGen = nGen
        self.rMutation = rMutation
        self.nIter = nIter
        self.pSel = pSel
        self.sSel = sSel
        # Initialize population
        self.population = []
        self.parents = []
        self.survivors = []
        # Statistics
        self.bestFitnesses = []
        self.avgFitnesses = []

    def readFile(self, fileName):
        f = open(fileName, "r")
        lines = f.readlines()
        f.close()
        return lines

    def mutation(self, chromosomes):
        for i in range(len(chromosomes)):
            if rd.random() < self.rMutation:
                np.random.shuffle(chromosomes[i].genes)

    def crossover(self):
        pass

    def parentSelection(self):
        if self.pSel == "fp":
            self.parents = self.fitnessProp(self.nOffSpring*2)
        elif self.pSel == "rb":
            self.parents = self.rankBased(self.nOffSpring*2)
        elif self.pSel == "bt":
            self.parents = self.binaryTournament(self.nOffSpring*2)
        elif self.pSel == "tr":
            self.parents = self.truncation(self.nOffSpring*2)
        elif self.pSel == "rd":
            self.parents = self.random(self.nOffSpring*2)
        else:
            error("Invalid parent selection scheme")

    def survivalSelection(self):
        if self.sSel == "fp":
            self.survivors = self.fitnessProp(self.nPop)
        elif self.sSel == "rb":
            self.survivors = self.rankBased(self.nPop)
        elif self.sSel == "bt":
            self.survivors = self.binaryTournament(self.nPop)
        elif self.sSel == "tr":
            self.survivors = self.truncation(self.nPop)
        elif self.sSel == "rd":
            self.survivors = self.random(self.nPop)
        else:
            error("Invalid survival selection scheme")

    # Selection schemes for parent and survivor selection

    def fitnessProp(self, N):
        fitnessSum = sum([i.fitness for i in self.population])
        fitnessProb = [i.fitness/fitnessSum for i in self.population]
        return list(np.random.choice(self.population, N, p=fitnessProb, replace=False))

    def rankBased(self, N):
        pass

    def binaryTournament(self, N):
        finalPopulation = []
        while(len(finalPopulation) < N):
            c1 = rd.choice(self.population)
            c2 = rd.choice(self.population)
            if c1.fitness > c2.fitness:
                if c1 in finalPopulation:
                    continue
                finalPopulation.append(c1)
            else:
                if c2 in finalPopulation:
                    continue
                finalPopulation.append(c2)
        return finalPopulation

    def truncation(self, N): return self.sortFitness()[:N]

    def random(self, N): return list(
        np.random.choice(self.population, N, replace=False))

    def compFitnessAll(self):
        for i in range(self.nPop):
            self.population[i].fitness = self.compFitness(
                self.population[i].genes)

    def sortFitness(self): return sorted(self.population,
                                         key=lambda x: x.fitness, reverse=True)

    def bestFitness(self): return max([i.fitness for i in self.population])

    def avgFitness(self): return sum(
        [i.fitness for i in self.population])/self.nPop

    def plot(self):
        plt.plot(self.bestFitnesses)
        plt.plot(self.avgFitnesses)
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.legend(["Average Best Fitness over " + str(self.nIter) + " iterations",
                    "Average Fitness over " + str(self.nIter) + " iterations"])
        plt.savefig("plot.png")

    def run(self):
        for i in range(self.nIter):
            self.popInit()
            bestFitness = 0
            avgFitness = 0
            for j in range(self.nGen):
                self.parentSelection()
                self.crossover()
                self.compFitnessAll()
                self.survivalSelection()
                self.population = self.survivors
                self.survivors = []

                bestFitness += self.bestFitness()
                avgFitness += self.avgFitness()

            self.bestFitnesses.append(bestFitness/self.nIter)
            self.avgFitnesses.append(avgFitness/self.nIter)
