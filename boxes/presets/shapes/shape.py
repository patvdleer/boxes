
class Shape:
    _n_dimensions: int

    def is_2D(self):
        return self._n_dimensions == 2

    def is_3D(self):
        return self._n_dimensions == 3
