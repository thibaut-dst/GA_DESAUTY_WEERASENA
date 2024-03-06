# Genetic Algorithm Solver Module

This module provides a framework for solving optimization problems using genetic algorithms (GA). It was developed for the PW3/TP3 as part of the profesionnal programming course run by Ms T. Drumond.


## 1. Classes

### Individual

Represents an individual in the GA population.

Methods:
* __init__(chromosome: list, fitness: float): Initializes an individual.
* __lt__(other): Comparator based on fitness.
* __repr__(): String representation.

### GAProblem

Defines a GA problem. Users need to implement the functions inside this class  for their specific problems.

Methods:
* single_chromosome_initialization(): Initialize a chromosome.
* computeFiness(chromosome): Compute fitness.
* reproduction(population): Reproduction method.
* mutation(new_chrom, mutation_rate): Mutation method.

### GASolver

Implements the GA solving process with generic functions.

Methods:
* __init__(problem: GAProblem, selection_rate=0.5, mutation_rate=0.1): Initializes the solver.
* reset_population(pop_size=5000): Initializes the population.
* selection(): Selection process.
* evolve_for_one_generation(): Evolution for one generation.
* get_best_individual(): Returns the best individual.
* show_generation_summary(): Prints population summary.
* evolve_until(max_nb_of_generations=500, threshold_fitness=None): Evolution until termination

## 2. Usage

* Define problem by subclassing GAProblem.
* Implement functions in GAProblem for a given problem.
* Instantiate problem.
* Create a solver instance with the problem.
* Customize solver parameters.
* Reset population.
* Evolve population.


## 3. Example Implementations

Two example implementations are provided for guidance in the examples folder:

mastermind_problem.py: Solves the Mastermind game using the module.
tsp_problem.py: Solves the Traveling Salesman Problem using the module.
