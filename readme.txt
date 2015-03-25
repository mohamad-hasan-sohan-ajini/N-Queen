################################
##########in his name###########
################################
operators.py
this module contains some premitive operators manipulating chromosomes.
these operators defined according to the related N-Queen slides.

GA.py
it contains a genetic algorithm class that is able to solve problem 
by means of operators and its methods.

test.py
it creates a GA instance and solve N-Queen problem by calling a method of GA.

notices:
1- all operators are defined as described in N-Queen slides.
2- main parameters including queen numbers (i.e. board size), population 
size and maximum calculation of evaluation function will be easily manipulated
by passing a simple value to __init__ and solver methods.

