class FoodSource:
    def __init__(self, value):
        self.value = value
        self.trials = 0

    def __repr__(self):
        return "(Value of food source [%s] with trials [%s])" % (self.value, self.trials)

    def increment_trial(self):
        self.trials = self.trials + 1
