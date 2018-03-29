import math

from libs.point import Point


__all__ = ['Vector', 'get_angle']


class Vector(Point):
    @staticmethod
    def from_p(a: Point, b: Point):
        return Vector(b.x - a.x, b.y - a.y)

    def __str__(self):
        return '(x: {}, y:{}'.format(self.x, self.y)


def get_angle(a: Vector, b: Vector):
    sin = a.x * b.y - b.x * a.y
    cos = a.x * b.x + a.y * b.y
    return math.atan2(sin, cos) * (180 / math.pi)
