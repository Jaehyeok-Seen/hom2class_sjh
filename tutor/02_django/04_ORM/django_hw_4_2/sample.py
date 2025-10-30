class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangular:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

point_1 = Point(0, 0)
point_2 = Point(2, 2)

r1 = Rectangular(point_1, point_2)

point_3 = [6, 5, 4]
r2 = Rectangular(point_3, [])
r2.p1.sort()
print(r2.p1)
