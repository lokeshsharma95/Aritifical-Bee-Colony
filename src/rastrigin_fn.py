from src import objective_fn
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D



class rastrigin_fn(objective_fn):

    def __init__(self, dims):
        super(rastrigin_fn, self).__init__(dims)


    def get_minima(self):
        return 0


    def eval_fn(self, params):
        A = 10
        f = 0
        try:
            if (len(params) != self.dims):
                raise Exception('number of paramters passd is not the same as the number of expected dimensions')

            for i in range(0, len(params)):
                f = f + A + (params[i]**2 - (A * math.cos(2 * math.pi * params[i])))

            return f
        except Exception as error:
            print('Exception raised in rastrigin_fn.eval_fn: ', repr(error))


    def graph_fn(self):
        A = 10
        X = np.linspace(-5.12, 5.12, 200)
        Y = np.linspace(-5.12, 5.12, 200)

        X, Y = np.meshgrid(X, Y)

        Z = A + sum([x**2 - A * np.cos(2 * math.pi * x) for x in X]) + sum([y**2 - A * np.cos(2 * math.pi * y) for y in Y])

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)
        plt.savefig('rastrigin.png')
