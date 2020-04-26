from src.FoodSource import FoodSource
import numpy as np


class ABC:
    def __init__(self, population, fitness_function, employed_bee_percentage=0.5, runs=20, lower_bound=[-10, -10],
                 upper_bound=[10, 10], rounding_factor=2):
        assert len(lower_bound) == len(upper_bound)
        self.population = population
        self.fitness_function = fitness_function
        self.employed_bee_percentage = employed_bee_percentage
        self.runs = runs
        self.lower_bound = np.array(lower_bound)
        self.upper_bound = np.array(upper_bound)
        self.rounding_factor = rounding_factor

        self.employed_bees = round(population * employed_bee_percentage)
        self.onlooker_bees = population - self.employed_bees
        self.food_source = self.initialise_food_source()

    def initialise_food_source(self):
        initial_food_source = []
        for i in range(self.employed_bees):
            value = np.random.uniform(self.lower_bound, self.upper_bound)
            value = np.around(value, decimals=self.rounding_factor)
            initial_food_source.append(FoodSource(value))
        return initial_food_source
