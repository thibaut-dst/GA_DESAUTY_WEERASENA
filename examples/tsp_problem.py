# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from ga_solver import GAProblem
import cities as cities
import random
from ga_solver import GASolver
from ga_solver import Individual

class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""
    
    def single_chromosome_initialization(self):
        chromosome = cities.default_road(city_dict)
        random.shuffle(chromosome)
        return chromosome
    
    def computeFiness(self, chromosome):
        return (-1*cities.road_length(city_dict, chromosome))


    def reproduction(self, population_list):
        nb_random1 = random.randrange(0, 24)
        nb_random2 = nb_random1
        while nb_random2 == nb_random1:
            nb_random2 = random.randrange(0, 24)
        
        a = population_list[nb_random1] # this is a random individual in the population list
        b = population_list[nb_random2] # this is a second random individual in the population list

        new_chrom = a.chromosome[:(len(a.chromosome)//2)] + [x for x in b.chromosome[(len(b.chromosome)//2):] if x not in a.chromosome[:(len(a.chromosome)//2)]]

        possible_cities = cities.default_road(city_dict)
        if len(new_chrom) != len(a.chromosome):
            for city in possible_cities:
                if city not in new_chrom:
                    new_chrom.append(city)
        
        return new_chrom


    def mutation(self, new_chrom, mutation_rate):
        nb = random.random()
        if nb < mutation_rate:
            random_position1 = random.randrange(0, len(new_chrom))
            random_position2 = random_position1
            while random_position2 == random_position1:
                random_position2 = random.randrange(0, len(new_chrom))
            new_chrom[random_position1], new_chrom[random_position2] = new_chrom[random_position2], new_chrom[random_position1] 
            
        return Individual(new_chrom, self.computeFiness(new_chrom))


if __name__ == '__main__':

    city_dict = cities.load_cities("cities.txt")
    problem = TSProblem()
    solver = GASolver(problem)
    solver.reset_population(pop_size=100)
    solver.evolve_until()
    best = solver.get_best_individual()
    print(best)
    cities.draw_cities(city_dict, best.chromosome)
