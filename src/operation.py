"""
operation.py --- Operators for Genetic Algorithm
- tournament: selection operator, using tournament selection
- mutation: mutation operator, exchanging indices from each partitions
- crossover: crossover operator, single point crossover
"""

import random as rd
import copy
import sys
from src.evalutation import fitness


# selection operator: tournament selection
def tournament(pop, bestCut, worstCut, k):
    copiedPop = copy.deepcopy(pop)

    # tournament for parent 1
    candidates = rd.choices(copiedPop, k=k)
    bestFit = sys.maxsize
    bestIdx = 0

    for idx in range(len(candidates)):
        currentFit = fitness(worstCut, bestCut, pop[idx])
        if bestFit < currentFit:
            bestFit = currentFit
            bestIdx = idx

    copiedPop.remove(copiedPop[bestIdx])
    parent1 = copiedPop[bestIdx]

    # tournament for parent 2
    candidates = rd.choices(copiedPop, k=k)
    bestFit = sys.maxsize
    bestIdx = 0

    for idx in range(len(candidates)):
        currentFit = fitness(worstCut, bestCut, pop[idx])
        if bestFit < currentFit:
            bestFit = currentFit
            bestIdx = idx

    parent2 = copiedPop[bestIdx]

    return parent1, parent2


def mutation(ind):
    mutatedInd = copy.deepcopy(ind)

    part0 = [index for index in range(len(ind)) if mutatedInd[index] == 0]  # partition 0
    part1 = [index for index in range(len(ind)) if mutatedInd[index] == 1]  # partition 1

    mutIdx0 = rd.choice(part0)
    mutIdx1 = rd.choice(part1)

    # swap indices
    mutatedInd[mutIdx0], mutatedInd[mutIdx1] = mutatedInd[mutIdx1], mutatedInd[mutIdx0]

    return mutatedInd


# single point cross-over
def crossover(parent1, parent2):
    pivot = rd.choice(range(len(parent1)))

    offspring1 = parent1[:pivot] + parent2[pivot:]
    offspring2 = parent2[:pivot] + parent1[pivot:]

    return offspring1, offspring2