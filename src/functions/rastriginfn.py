from src.functions.objectivefn import ObjectiveFn
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


class RastriginFn(ObjectiveFn):

    def __init__(self, dims):
        super(RastriginFn, self).__init__(dims)
        self.domain = (-5.12, 5.12)

    def get_minima(self):
        minima_coords = [0 for i in range(self.dims)]  # Function value is 0 here.
        minima = tuple(minima_coords)
        return self.evaluate(minima)

    def evaluate(self, params):
        A = 10
        f = 0
        try:
            if len(params) != self.dims:
                raise Exception('number of paramters passd is not the same as the number of expected dimensions')

            for param in params:
                f = f + A + (param ** 2 - (A * math.cos(2 * math.pi * param)))

            return f
        except Exception as error:
            print('Exception raised in rastrigin_fn.eval_fn: ', repr(error))

    def eval_vectors(self, *X, **kwargs):
        A = kwargs.get('A', 10)
        return A + sum([(x ** 2 - A * np.cos(2 * math.pi * x)) for x in X])

    def graph_fn(self):
        A = 10
        X = np.linspace(-5.12, 5.12, 200)
        Y = np.linspace(-5.12, 5.12, 200)

        X, Y = np.meshgrid(X, Y)

        Z = self.eval_vectors(X, Y, A=10)

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)
        plt.savefig('rastrigin.png')

    def contour_plot(self, save_file_name, points):
        A = 10
        # X = np.linspace(-5.12, 5.12, 200)
        # Y = np.linspace(-5.12, 5.12, 200)
        X = np.linspace(self.domain[0], self.domain[1], 200)
        Y = np.linspace(self.domain[0], self.domain[1], 200)

        X, Y = np.meshgrid(X, Y)

        Z = self.eval_vectors(X, Y, A=10)
        plt.contour(X, Y, Z)
        for point in points:
            # print(point)
            plt.scatter(point[0], point[1], marker='X', color='r')
        plt.savefig(save_file_name, dpi=300, bbox_inches='tight')
        plt.close()

    def is_defined_only_for_2d(self):
        return False

    def name(self):
        return "rastrigin"