# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from ga_solver import GAProblem
import examples.mastermind as mm
import random
from typing import List
from ga_solver import GASolver
from ga_solver import Individual


class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""

    def single_chromosome_initialization(self):
        return mm.generate_random_secret(size=4)
    
    def computeFiness(self, chromosome):
        return match.rate_guess(chromosome)


    def reproduction(self, population_list):
        nb_random1 = random.randrange(0, 24)
        nb_random2 = nb_random1
        while nb_random2 == nb_random1:
            nb_random2 = random.randrange(0, 24)
        
        a = population_list[nb_random1] # this is a random individual in the population list
        b = population_list[nb_random2] # this is a second random individual in the population list

        x_point = random.randrange(0, len(a.chromosome))
        new_chrom = a.chromosome[0:x_point] + b.chromosome[x_point:]
        return new_chrom


    def mutation(self, new_chrom, mutation_rate):
        nb = random.random()
        if nb < mutation_rate:
            random_position = random.randrange(0, len(new_chrom))
            valid_colors = mm.get_possible_colors()
            new_gene = random.choice(valid_colors)
            new_chrom = new_chrom[0:random_position] + [new_gene] + new_chrom[random_position+1:]
       
        return Individual(new_chrom, self.computeFiness(new_chrom))
    


if __name__ == '__main__':

    match = mm.MastermindMatch(secret_size=4)
    problem = MastermindProblem()
    solver = GASolver(problem)

    solver.reset_population(pop_size=5000)
    solver.evolve_until()

    best = solver.get_best_individual()
    print(best)
    print(f"Problem solved? {match.is_correct(best.chromosome)}")