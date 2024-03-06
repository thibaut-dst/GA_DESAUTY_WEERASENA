# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(generic genetic algorithm module)
"""

class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm

        Args:
            chromosome (list[]): a list representing the individual's
            chromosome
            fitness (float): the individual's fitness (the higher the value,
            the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GAProblem:
    """Defines a Genetic algorithm problem to be solved by ga_solver"""

    def single_chromosome_initialization(self):
        """
        Initialize a single chromosome with the appropriate size for the problem.

        Returns:
            list: A chromosome representing an individual in the population.
        """
        pass

    def computeFiness(self, chromosome):
        """
        Compute the fitness score of a given chromosome.

        Args:
            chromosome (list): The chromosome to evaluate.

        Returns:
            float: The fitness score of the chromosome.
        """
        pass

    def reproduction(self, population):
        """
        Perform reproduction to create a new chromosome based on selected individuals from the population.
        Combine genetic material from parent individuals in the population to generate new individuals for the next generation.

        Args:
            population_list (list of Individual): The current population of individuals.

        Returns:
            list: A new chromosome created through crossover of selected individuals.
        """
        pass

    def mutation(self, new_chrom, mutation_rate):
        """
        Apply mutation to the given chromosome with a certain mutation rate.
        This method introduces random changes in the chromosome to promote genetic diversity.
        
        Args:
            new_chrom (list): The chromosome on which mutation may be applied.
            mutation_rate (float): The probability of mutation, between 0 and 1.

        Returns:
            Individual: A new Individual with the mutated chromosome.
        """
        pass
    

class GASolver:
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            problem (GAProblem): GAProblem to be solved by this ga_solver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []


    def reset_population(self, pop_size=5000):
        """ Initialize the population with pop_size random Individuals """
        for i in range(pop_size): #we create as many indivuals that pop_size says
            chromosome = self._problem.single_chromosome_initialization()
            fitness = self._problem.computeFiness(chromosome)
            new_individual = Individual(chromosome, fitness)
            self._population.append(new_individual)


    def selection(self):
        self._population.sort(reverse=True)
        population_selected_size = int(len(self._population) * self._selection_rate)
        selected_population = self._population[:population_selected_size]
        self._population = selected_population

    def evolve_for_one_generation(self):
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Selection: Remove x% of population (less adapted)
            -   Reproduction: Recreate the same quantity by crossing the 
                surviving ones 
            -	Mutation: For each new Individual, mutate with probability 
                mutation_rate i.e., mutate it if a random value is below   
                mutation_rate
        """
        self.selection() #sort and selection 
        new_chrom = self._problem.reproduction(self._population)
        new_individual = self._problem.mutation(new_chrom, self._mutation_rate)
        self._population.append(new_individual)

    def get_best_individual(self):
        """ Return the best Individual of the population """
        self._population.sort(reverse=True)
        return self._population[0]

    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        for individual in self._population:
            print(individual)

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        best_individual = self.get_best_individual()
        
        while (max_nb_of_generations <= 500) :
            if threshold_fitness != None:
                if best_individual.fitness>=threshold_fitness:
                    break 
            self.evolve_for_one_generation()
            best_individual = self.get_best_individual()
            max_nb_of_generations+=1