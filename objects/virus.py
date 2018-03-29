from libs.point import Point


class Virus:
    def __init__(self, item):
        self.pos = Point(item.get('X'), item.get('Y'))
        self.mass = item.get('M')
        self.id = item.get('Id')
