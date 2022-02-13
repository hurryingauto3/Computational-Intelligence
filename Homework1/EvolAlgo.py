# Class of generic evolutionary algorithm
from logging import error
from random import random, randint, choice
import numpy as np
import pandas as pd


class SelectionScheme:
    @staticmethod

    def fitnessProp(population, fitness):
        pass

    def rankBased(population):
        pass

    def binaryTournament():
        pass

    def truncation():
        pass

    def random():
        pass

class EvolAlgo:
    def __init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme):

        self.fileData = self.readFile(fileName)
        self.selScheme = selScheme
        self.popSize = popSize
        self.numoffSpring = numoffSpring
        self.numGen = numGen
        self.mutRate = mutRate
        self.numIter = numIter
        self.pop = []
        pass

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
    
    def selScheme(self):
        if self.selScheme == "fp":
            SelectionScheme.fitnessProp(self.pop, self.compFitness())
        elif self.selScheme == "rb":
            SelectionScheme.rankBased()
        elif self.selScheme == "bt":
            SelectionScheme.binaryTournament()
        elif self.selScheme == "tr":
            SelectionScheme.truncation()
        elif self.selScheme == "rd":
            SelectionScheme.random()
        else:
            error("Invalid selection scheme")
        pass

    def compFitnessAll(self):
        popFitness = []
        for i in range(len(self.popSize)):
            popFitness.append(self.compFitness(self.pop[i]))
        return popFitness   

    def compFitness(self):
        pass

    def run(self):

        for i in range(self.numIter):
            for i in range(self.popInit):
                self.pop.append(self.crossover())
        pass



