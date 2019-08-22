class Circle():
    def __init__(self, radius):
        self._radius = radius
        self._surface_area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def surface_area(self):
        self.surface_area = self.surface_area_circle()
        return self.surface_area

    @surface_area.setter
    def surface_area(self, value):
        self._surface_area = value

    def surface_area_circle(self):
        return 3.14 * self.radius *  self.radius