import imp
from knapsack import knapsack
from graphcol import graphcoloring
from tsp import tsp

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

    gc = graphcoloring("gc-ds.txt",nPop, nOffspring, nGen, rMutation, nIter, i[0], i[1], True)
    gc.run()
    gc.plot("Total Violations", "report/images/graphcoloring_"+i[0]+"_"+i[1])
    del gc

    tsp = tsp("tsp-ds.tsp", nPop, nOffspring, nGen, rMutation, nIter, i[0], i[1], True)
    tsp.run()
    tsp.plot("Total Distance", "report/images/tsp_"+i[0]+"_"+i[1])
    del tsp

