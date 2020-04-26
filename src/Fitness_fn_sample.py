class SimpleFitnessFunction:
    def __init__(self):
        pass

    def evaluate(self, value):
        x = value[0]
        y = value[1]
        return x * x + y * y
