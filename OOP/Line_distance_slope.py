class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return (((li.coor2[0]-li.coor1[0])**2) + ((li.coor2[1]-li.coor1[1])**2))**(.5)

    def slope(self):
        return (li.coor2[1]-li.coor1[1])/(li.coor2[0]-li.coor1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print('distance',li.distance())
print('slope',li.slope())