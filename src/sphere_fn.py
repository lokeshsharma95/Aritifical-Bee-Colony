from src.objective_fn import objective_fn
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


class sphere_fn(objective_fn):

    def __init__(self, dims):
        super(sphere_fn, self).__init__(dims)
        # self.domain = (-math.inf, math.inf)
        self.domain = (-10, 10)


    def get_minima(self):
        minima_coords = [0 for i in range(self.dims)]  # Function value is 0 here.
        minima = tuple(minima_coords)
        return self.eval_fn(minima)


    def eval_fn(self, params):
        f = 0
        try:
            if len(params) != self.dims:
                raise Exception('Dimensions not matching params')
            for param in params:
                f = f + (param ** 2)
            return f
        except Exception as error:
            print('Exception in sphere_fn.eval_fn: ', repr(error))


    def graph_fn(self):
        # X = np.linspace(-10, 10, 100)
        # Y = np.linspace(-10, 10, 100)
        X = np.linspace(self.domain[0], self.domain[1], 200)
        Y = np.linspace(self.domain[0], self.domain[1], 200)
        X, Y = np.meshgrid(X, Y)
        Z = X**2 + Y**2

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)
        plt.savefig('sphere.png')


    def contour_plot(self, save_file_name, points):
        # X = np.linspace(-10, 10, 100)
        # Y = np.linspace(-10, 10, 100)
        # X = np.linspace(-5, 5, 200)
        # Y = np.linspace(-5, 5, 200)
        X = np.linspace(self.domain[0], self.domain[1], 200)
        Y = np.linspace(self.domain[0], self.domain[1], 200)
        X, Y = np.meshgrid(X, Y)
        Z = X**2 + Y**2

        plt.contour(X, Y, Z)
        for point in points:
            plt.scatter(point[0], point[1], marker='X', color='red')
        plt.savefig(save_file_name, dpi=300, bbox_inches='tight')
        plt.close()


    def is_defined_only_for_2d(self):
        return False