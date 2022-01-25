from math import sqrt

class Circle:

    def __init__(self, centre, r):
        self.centre = centre
        self.radius = r
    
    def __contains__(self, coords):
        if (coords[0]-self.centre[0])**2 + (coords[1]-self.centre[1])**2 < self.radius**2:
            return True
        else:
            return False
