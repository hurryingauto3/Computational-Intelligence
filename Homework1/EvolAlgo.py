# Class of generic evolutionary algorithm
from logging import error
from random import random, randint, choice
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class SelectionScheme:
    @staticmethod

    def fitnessProp(fitness):
        pass

    def rankBased(fitness):
        pass

    def binaryTournament():
        pass

    def truncation(fitness):
        popFitness = [(k,v) for k,v in fitness.items()]


        print(popFitness)
            


        
    def random():
        pass

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
    
    def schemeSel(self):
        if self.selScheme == "fp":
            return SelectionScheme.fitnessProp(self.compFitness())
        elif self.selScheme == "rb":
            return SelectionScheme.rankBased()
        elif self.selScheme == "bt":
            return SelectionScheme.binaryTournament()
        elif self.selScheme == "tr":
            return SelectionScheme.truncation(self.sortFitness())
        elif self.selScheme == "rd":
            return SelectionScheme.random()
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

    def compFitness(self, gene):
        pass

    def run(self):

        for i in range(self.numIter):
            self.popInit()
            self.compFitnessAll()
            self.selScheme()
            self.crossover()
            self.mutation()
        pass



