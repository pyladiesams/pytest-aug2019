class Circle():
    def __init__(self, radius):
        self.__radius = radius
        self.__surface_area = None

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    @property
    def surface_area(self):
        self.__surface_area = self.surface_area_circle()
        return self.__surface_area

    @surface_area.setter
    def surface_area(self, value):
        self.__surface_area = value

    def surface_area_circle(self):
        return 3.14 * self.radius * self.radius