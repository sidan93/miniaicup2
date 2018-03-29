from libs.point import Point


class Food:
    mass = 1.0

    def __init__(self, item):
        self.pos = Point(item.get('X'), item.get('Y'))
