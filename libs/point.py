import math

__all__ = ['Point', 'dist']


class Point:
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __str__(self):
        return 'x: {}, y: {}'.format(self.x, self.y)


def dist(a: Point, b: Point):
    return math.sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y))
