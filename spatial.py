import math

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector2D(self.x-other.x, self.y-other.y)

    def __mul__(self, value):
        return Vector2D(self.x*value, self.y*value)

    def __truediv__(self, value):
        return Vector2D(self.x/value, self.y/value)

    def root(self):
        rx = 0
        ry = 0
        if self.x > 0:
            rx = math.sqrt(self.x)
        if self.y > 0:
            ry = math.sqrt(self.y)
        return Vector2D(rx, ry)
        
    def square(self):
        return Vector2D(self.x*self.x, self.y*self.y)

    def mag(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def normalise(self):
        return self*(1/self.mag())
        
    def bearing(self):
        return math.atan2(self.x, self.y)

    def dot(self, other):
        return self.x*other.x+self.y*other.y

    def cross(self,other):
        return self.x*other.y-self.y*other.x

    def distance(self, other):
        return other.sub(self).mag()

    def quadrance(self, other):
        return (other.x-self.x)*(other.x-self.x)+(other.y-self.y)*(other.y-self.y)

    @staticmethod
    def fromBearing(angle):
        return Vector2D(math.cos(angle), math.sin(angle))

class Limits():
    
    def __init__(self, min_point, max_point):
        self.min_point = min_point
        self.max_point = max_point

    def contains(self, pos):
        if (pos.x < self.min_point.x):
            return False
        if (pos.y < self.min_point.y):
            return False
        if (pos.x > self.max_point.x):
            return False
        if (pos.y > self.max_point.y):
            return False
        return True