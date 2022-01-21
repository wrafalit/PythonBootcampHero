class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return (self.radius * self.radius * self.height * Cylinder.pi)

    def surface_area(self):
        pass


# EXAMPLE OUTPUT
c = Cylinder(2, 3)
print('volume ', c.volume())