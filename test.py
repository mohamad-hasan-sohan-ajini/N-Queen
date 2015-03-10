# -*- coding: utf-8 -*-

import GA

#default values for GA: pop_size=100, n=8 (solving 8 queen)
my_ga = GA.GA()
# default values for solver: max_eval=10000, random_selections=5 (select 5 candid parent
# randomly and choose 2 best of them for mating)
my_ga.solver(max_eval=30000)
