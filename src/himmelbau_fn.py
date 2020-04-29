from src import objective_fn
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


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
        # X = np.linspace(-10, 10, 100)
        # Y = np.linspace(-10, 10, 100)
        X = np.linspace(self.domain[0], self.domain[1], 200)
        Y = np.linspace(self.domain[0], self.domain[1], 200)
        X, Y = np.meshgrid(X, Y)
        Z = (X**2 + Y - 11)**2 + (X + Y**2 - 7)**2

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)
        plt.savefig('himmelbau.png')


    def contour_plot(self, save_file_name, points):
        # X = np.linspace(-10, 10, 100)
        # Y = np.linspace(-10, 10, 100)
        X = np.linspace(self.domain[0], self.domain[1], 200)
        Y = np.linspace(self.domain[0], self.domain[1], 200)
        X, Y = np.meshgrid(X, Y)
        Z = (X**2 + Y - 11)**2 + (X + Y**2 - 7)**2

        plt.contour(X, Y, Z)
        for point in points:
            plt.scatter(point[0], point[1], marker='X', color='red')
        plt.savefig(save_file_name, dpi=300)


    def is_defined_only_for_2d(self):
        return True