# import pyswarms as ps
# from pyswarms.utils.functions import single_obj as fx
import matplotlib.pyplot as plt
import random 

class PSO:
    
    def __init__(self, n_particles, n_dimensions, bounds, fx, fx_args, max_iter, verbose=False):
        self.n_particles = n_particles
        self.n_dimensions = n_dimensions
        self.bounds = bounds
        self.fx = fx
        self.fx_args = fx_args
        self.max_iter = max_iter
        self.verbose = verbose

        self.pos = [[random.randdom() for _ in range(self.n_dimensions)] for _ in range(self.n_particles)]
        self.velocity = [[0 for _ in range(self.n_dimensions)] for _ in range(n_particles)]
        self.pBest = []
        self.fitness = []

        pass

    def compFitness():
        pass


    # def compFitnessAll(self):
    #     for i in range(self.nPop):
    #         self.population[i].fitness = self.compFitness(
    #             self.population[i].genes)

    # def sortFitness(self): return sorted(self.population, key=lambda x: x.fitness)

    # def bestFitness(self):
    #     if self.minimize:
    #         return min([i.fitness for i in self.population])
    #     else:
    #         return max([i.fitness for i in self.population])

    # def avgFitness(self): return sum([i.fitness for i in self.population])/self.nPop

    # def plot(self, fitness, name):
    #     plt.plot(self.bestFitnesses)
    #     plt.plot(self.avgFitnesses)
    #     plt.xlabel("Generation")
    #     plt.ylabel("Fitness" + " (" +fitness + ")")
    #     plt.legend(["Average Best Fitness over " + str(self.nIter) + " iterations",
    #                 "Average Fitness over " + str(self.nIter) + " iterations"])
    #     plt.savefig(name+".png")
    #     plt.close()

    def updateVelocity(self):
        pass
    
    def popInit(self):
        pass

    def train(self):

        for i in range(self.max_iter):
            self.popInit()
            bestFitness = 0
            avgFitness = 0

            for j in range(self.n_particles):
                self.updateVelocity()
                self.pos[j] = self.pos[j] + self.velocity[j]
                self.pos[j] = self.pos[j] % 1
                self.fitness[j] = self.fx(self.pos[j], self.fx_args)
                if self.fitness[j] > bestFitness:
                    bestFitness = self.fitness[j]
                    self.pBest[j] = self.pos[j]
                avgFitness += self.fitness[j]
        pass

    def getMove():
        pass    





