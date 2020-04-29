from src import objective_fn
import math


class easom_fn(objective_fn):

    def __init__(self, dims):
        super(easom_fn, self).__init__(dims)
        self.domain = (-100, 100)


    def get_minima(self):
        minima_2d_coords = (math.pi, math.pi) # minima val is -1
        return self.eval_fn(minima_2d_coords)


    def eval_fn(self, params):
        f = 0
        try:
            if self.dims != 2:
                raise Exception('Dimensions more than 2')
            if self.dims != len(params):
                raise Exception('Dimensions not matching params')

            X = params[0]
            Y = params[1]
            f = -1 * math.cos(X) * math.cos(Y) * math.exp(-1 * ((X - math.pi)**2 + (Y - math.pi)**2))
            return f
        except Exception as error:
            print('Exception in easom_fn.eval: '. repr(error))


    def graph_fn(self):
        pass


    def is_defined_only_for_2d(self):
        return True