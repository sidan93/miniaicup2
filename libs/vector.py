import math

from libs.point import Point
from libs.utils import debug


__all__ = ['Vector', 'get_angle', 'in_angle']


class Vector(Point):
    @staticmethod
    def from_p(a: Point, b: Point):
        return Vector(b.x - a.x, b.y - a.y)

    @staticmethod
    def up():
        return Vector(0, -1)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        length = self.length()
        return Vector(self.x / length, self.y / length)


def get_angle(a: Vector, b: Vector, in_all: bool = True):
    sin = a.x * b.y - b.x * a.y
    cos = a.x * b.x + a.y * b.y
    angle = math.atan2(sin, cos) * (180 / math.pi)
    if angle < 0 and in_all:
        angle = 180 - angle
    return angle


def in_angle(cur, angle, check):
    left_border = cur - angle
    right_border = cur + angle
    if left_border < check < right_border:
        return True
    if left_border < 0:
        if 360 + left_border <= check <= 360:
            return True
    if right_border > 360:
        if 0 <= check <= right_border - 360:
            return True
    return False
