# -*- coding: utf-8 -*-

import random
import copy
import itertools
import math
import numpy as np

# Queen Existance Check, check if a queen exist in place
def qec(permutation, place):
    n = len(permutation)
    for i in range(n):
        selected_queen = (i, permutation[i])
        if selected_queen == place:
            return 1
    return 0

# fitness evaluation
def fitness(permutation):
    n = len(permutation)
    # assume that there is no row/col collision
    # this function will return diagonal gards only
    total_guards = 0
    for i in range(n):
        # selected queen coordinate
        sq_x = i
        sq_y = permutation[i]
        ch_y_u = sq_y
        ch_y_d = sq_y
        for ch_x in range(sq_x + 1, n):
            ch_y_u += 1
            ch_y_d -= 1
            if (ch_y_u < n) and (qec(permutation, (ch_x, ch_y_u))):
                total_guards += 1
            if (ch_y_u > 0) and (qec(permutation, (ch_x, ch_y_d))):
                total_guards += 1
    return total_guards

#recombine two parent and return two children
def recombination(permutation1, permutation2):
    n = len(permutation1)
    child1 = []
    child2 = []
    for i in range(n):
        child1.append(-1)
        child2.append(-1)
    # choose a random cross over point
    cross_over_point = random.randint(1, n - 1)
    # fill offsprings until cross over point
    for i in range(cross_over_point):
        child1[i] = permutation1[i]
        child2[i] = permutation2[i]
    # fill rest of the offspring
    # 'i' is child index
    for i in range(cross_over_point, n):
        # 'j' is parent index
        for j in range(n):
            if (not(permutation2[(j + cross_over_point) % n] in child1)
            and (child1[i] == -1)):
                child1[i] = permutation2[(j + cross_over_point) % n]
            if (not(permutation1[(j + cross_over_point) % n] in child2)
            and (child2[i] == -1)):
                child2[i] = permutation1[(j + cross_over_point) % n]
    return child1, child2

# mutate an individual
def mutation(permutation):
    n = len(permutation)
    rnd = random.random()
    mutation_prob = 0.8
    if rnd < mutation_prob:
        loci1 = random.randint(0, n - 1)
        loci2 = random.randint(0, n - 1)
        while loci2 == loci1:
            loci2 = random.randint(0, n - 1)
        result = copy.deepcopy(permutation)
        result[loci1], result[loci2] = result[loci2], result[loci1]
        return result
    return permutation

# generate a random n-permutation list
def generate_permutation(n):
    result = range(1, n + 1)
    np.random.shuffle(result)
    return result
    #return list(list(itertools.permutations(list(range(1, n + 1))))
    #[random.randint(0, math.factorial(n) - 1)])