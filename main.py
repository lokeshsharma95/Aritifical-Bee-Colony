from src.ABC import ABC
from src.Fitness_fn_sample import SimpleFitnessFunction

fitness_function = SimpleFitnessFunction()
abc = ABC(100, fitness_function, lower_bound=[-10, -10], upper_bound=[10, 10])
value = abc.run()
print(value)
