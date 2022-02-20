from knapsack import *
from graphcol import *
from tsp import *

selectionschemes = [('fp', 'rd'), ('bt', 'tr'), ('tr', 'tr'), ('rd', 'rd'),('fp', 'tr'), ('rb','bt'), ('rd', 'tr'), ('tr', 'rb'), ('rb', 'rd'), ('bt','fp')]

nPop = 30
nOffspring = 10
nGen = 100
rMutation = 0.5
nIter = 10

for i in selectionschemes:

    ks = knapsack("f2_l-d_kp_20_878", nPop, nOffspring, nGen, rMutation, nIter, i[0], i[1], False)
    ks.run()
    ks.plot("Total Value", "report/images/knapsack_"+i[0]+"_"+i[1])
    del ks
    print("Knapsack completed with " + i[0] + " and " + i[1] + " selection schemes")

    gc = graphcoloring("gc-ds.txt",nPop, nOffspring, nGen, rMutation, nIter, i[0], i[1], True)
    gc.run()
    gc.plot("Total Violations", "report/images/graphcoloring_"+i[0]+"_"+i[1])
    del gc
    print("Graph Coloring completed with " + i[0] + " and " + i[1] + " selection schemes")

    tsp = TSP("tsp-ds.tsp", nPop, nOffspring, nGen, rMutation, nIter, i[0], i[1], True)
    tsp.run()
    tsp.plot("Total Distance", "report/images/tsp_"+i[0]+"_"+i[1])
    del tsp
    print("TSP completed with " + i[0] + " and " + i[1] + " selection schemes")

