class ObjectiveFn:

    def __init__(self, dims):
        self.dims = dims

    def get_minima(self):
        pass

    def evaluate(self, params):
        pass

    def graph_fn(self):
        pass

    def contour_plot(self, save_file_name, points):
        pass

    def is_defined_only_for_2d(self):
        pass

    def name(self):
        pass
