from src import objective_fn
import math


class himmelbau_fn(objective_fn):

    def __init__(self):
        super(himmelbau_fn, self).__init__(2)
        self.domain = (-5.0, 5.0)


    def get_minima(self):
        # minima = (3.0, 2.0)             # Minima point 1
        # minima = (-2.805118, 3.131312)  # Minima point 2
        # minima = (-3.779310, -3.283186) # Minima point 3
        minima = (3.584428, -1.848126)  # Minima point 4
        return self.eval_fn(minima)     # minima value is 0 at the 4 global minimas


    def eval_fn(self, params):
        f = 0
        try:
            if len(params) != self.dims:
                raise Exception('Dimensions not matching params')
            X = params[0]
            Y = params[1]
            f = (X**2 + Y - 11)**2 + (X + Y**2 - 7)**2
            return f
        except Exception as error:
            print('Exception in sphere_fn.eval_fn: ', repr(error))


    def graph_fn(self):
        pass


    def is_defined_only_for_2d(self):
        return True