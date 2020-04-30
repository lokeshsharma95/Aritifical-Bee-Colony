from src.functions.objectivefn import ObjectiveFn
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


class EasomFn(ObjectiveFn):

    def __init__(self):
        super(EasomFn, self).__init__(2)
        self.domain = (-10, 10)

    def get_minima(self):
        minima_coords = [math.pi for i in range(self.dims)]  # minima val is -1
        minima = tuple(minima_coords)
        return self.evaluate(minima)

    def evaluate(self, params):
        f = 0
        try:
            if self.dims != 2:
                raise Exception('Dimensions more than 2')
            if self.dims != len(params):
                raise Exception('Dimensions not matching params')

            X = params[0]
            Y = params[1]
            f = -1 * math.cos(X) * math.cos(Y) * math.exp(-1 * ((X - math.pi) ** 2 + (Y - math.pi) ** 2))
            return f
        except Exception as error:
            print('Exception in easom_fn.eval: '.repr(error))

    def graph_fn(self):
        X = np.linspace(self.domain[0], self.domain[1], 200)
        Y = np.linspace(self.domain[0], self.domain[1], 200)
        X, Y = np.meshgrid(X, Y)
        Z = -1 * np.cos(X) * np.cos(Y) * np.exp(-1 * ((X - math.pi) ** 2 + (Y - math.pi) ** 2))

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)
        plt.savefig('easom.png')

    def contour_plot(self, save_file_name, points):
        X = np.linspace(self.domain[0], self.domain[1], 200)
        Y = np.linspace(self.domain[0], self.domain[1], 200)
        X, Y = np.meshgrid(X, Y)
        Z = -1 * np.cos(X) * np.cos(Y) * np.exp(-1 * ((X - math.pi) ** 2 + (Y - math.pi) ** 2))

        plt.contour(X, Y, Z)
        for point in points:
            plt.scatter(point[0], point[1], marker='X', color='red')
        plt.savefig(save_file_name, dpi=300, bbox_inches='tight')
        plt.close()

    def is_defined_only_for_2d(self):
        return True

    def name(self):
        return "Easomfn"