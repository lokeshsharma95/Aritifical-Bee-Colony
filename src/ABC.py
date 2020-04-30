import operator
from collections import OrderedDict

from src.FoodSource import FoodSource
import numpy as np
import random as rand


class ABC:
    def __init__(self, population, fitness_function, employed_bee_percentage=0.5, runs=20, lower_bound=[-10, -10],
                 upper_bound=[10, 10], rounding_factor=2, trials_allowed=5):
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
        self.food_source_fitness_mapping = OrderedDict()
        self.trials_allowed = trials_allowed
        self.best_food_source = None
        self.current_run = 1

    def get_initial_food_source(self):
        initial_food_source = set()
        while len(initial_food_source) < self.employed_bees:
            source = self.create_food_source()
            initial_food_source.add(source)
        return initial_food_source

    def create_food_source(self):
        value = np.random.uniform(self.lower_bound, self.upper_bound).round(decimals=self.rounding_factor)
        source = FoodSource(value)
        return source

    def run(self):
        self.initialise_employee_bee()
        for i in range(self.runs):
            self.send_onlooker_bees()
            self.send_scout_bees()
            self.current_run += 1
        return self.best_food_source.value

    def initialise_employee_bee(self):
        food_sources = self.get_initial_food_source()
        for fs in food_sources:
            self.food_source_fitness_mapping[fs] = self.get_fitness(fs)

    def get_fitness(self, fs):
        fitness = self.fitness_function.evaluate(fs.value)
        if fitness >= 0:
            fitness = 1 / (1 + fitness)
        return round(fitness, self.rounding_factor)

    def send_onlooker_bees(self):
        fitness_sum = sum(self.food_source_fitness_mapping.values())
        weighted_probabilities = [round(individual_fitness / fitness_sum, self.rounding_factor) for individual_fitness
                                  in
                                  self.food_source_fitness_mapping.values()]
        for i in range(self.onlooker_bees):
            selected_index = rand.choices(range(len(self.food_source_fitness_mapping)), weights=weighted_probabilities)[
                0]
            selected_source = list(self.food_source_fitness_mapping.keys())[selected_index]
            new_source = self.generate_nearby_food_source(selected_source)
            self.get_best_solution(selected_source, new_source)

    def send_scout_bees(self):
        self.best_food_source = self.get_best_source()
        removed_count = 0
        added_count = 0
        food_source_to_pop = []
        self.plot_food_source()
        for food_source in self.food_source_fitness_mapping:
            if food_source.trials > self.trials_allowed:
                food_source_to_pop.append(food_source)
                removed_count += 1
        for food_source in food_source_to_pop:
            self.food_source_fitness_mapping.pop(food_source)
        if self.current_run > (self.runs * 3) / 4:
            return
        while added_count < removed_count:
            new_food_source = self.create_food_source()
            if new_food_source not in self.food_source_fitness_mapping:
                self.food_source_fitness_mapping[new_food_source] = self.get_fitness(new_food_source)
                added_count += 1

    def get_best_source(self):
        return max(self.food_source_fitness_mapping.items(), key=operator.itemgetter(1))[0]

    def get_best_solution(self, solution, new_solution):
        fitness_of_new_solution = self.get_fitness(new_solution)
        if self.food_source_fitness_mapping[solution] > fitness_of_new_solution:
            solution.increment_trial()
            return solution
        else:
            self.food_source_fitness_mapping[new_solution] = fitness_of_new_solution
            self.food_source_fitness_mapping.pop(solution)
        return new_solution

    def generate_nearby_food_source(self, food_source):
        solution = food_source.value
        k_source_index = rand.randint(0, len(self.food_source_fitness_mapping) - 1)
        k_solution = list(self.food_source_fitness_mapping.keys())[k_source_index].value
        d = rand.randint(0, len(self.lower_bound) - 1)
        r = rand.uniform(-1, 1)

        new_solution = np.copy(solution)
        new_solution[d] = solution[d] + r * (solution[d] - k_solution[d])
        if not self.lower_bound[d] <= new_solution[d] <= self.upper_bound[d]:
            new_solution[d] = round(np.random.uniform(self.lower_bound[d], self.upper_bound[d]), self.rounding_factor)

        return FoodSource(np.around(new_solution, decimals=self.rounding_factor))

    def plot_food_source(self):
        list_to_plot = []
        for food_source in self.food_source_fitness_mapping:
            list_to_plot.append(tuple(food_source.value))
        print(self.food_source_fitness_mapping)
        self.fitness_function.contour_plot("src/plots/"+ self.fitness_function.name() + str(self.current_run) + ".jpeg", list_to_plot)
