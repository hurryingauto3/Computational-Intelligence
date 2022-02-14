# Class of generic evolutionary algorithm
from logging import error
from random import random, randint, choice
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
    @staticmethod
    def __init__(self, fileName, popSize, numoffSpring, numGen, mutRate, numIter, selScheme):

        self.fileData = self.readFile(fileName)
        self.selScheme = selScheme
        self.popSize = popSize
        self.numoffSpring = numoffSpring
        self.numGen = numGen
        self.mutRate = mutRate
        self.numIter = numIter
        self.pop = []
        self.popFitness = []
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
            return SelectionScheme.fitnessProp(self.pop, self.compFitness())
        elif self.selScheme == "rb":
            return SelectionScheme.rankBased()
        elif self.selScheme == "bt":
            return SelectionScheme.binaryTournament()
        elif self.selScheme == "tr":
            return SelectionScheme.truncation()
        elif self.selScheme == "rd":
            return SelectionScheme.random()
        else:
            error("Invalid selection scheme")
        pass

    def compFitnessAll(self):

        for i in range(len(self.popSize)):
            self.popFitness.append(self.compFitness(self.pop[i]))

    def compFitness(self):
        pass

    def run(self):

        for i in range(self.numIter):
            self.popInit()
            self.compFitnessAll()
            self.selScheme()
            self.crossover()
            self.mutation()
        pass



