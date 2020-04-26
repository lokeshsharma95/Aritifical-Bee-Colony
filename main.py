from src.ABC import ABC
from src.Fitness_fn_sample import SimpleFitnessFunction

fitness_function = SimpleFitnessFunction()
abc = ABC(10, fitness_function, runs=10, lower_bound=[-10, -10], upper_bound=[10, 10])
value = abc.run()
print(value)
