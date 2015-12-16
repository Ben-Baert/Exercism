class TriangleError(ValueError):
    pass

class Triangle:
    def __init__(self, x, y, z):
        sides = sorted([x, y, z])
        if any(side <= 0 for side in sides):
            raise TriangleError("Sides should have a positive length")
        self.x, self.y, self.z = sides
        if (self.x + self.y) <= self.z:
            raise TriangleError

    def kind(self):
        if self.x == self.y == self.z:
            return "equilateral"
        if self.x == self.y or self.x == self.z or self.y == self.z:
            return "isosceles"
        return "scalene"