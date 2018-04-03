from libs.point import Point


class Virus:
    radius = 15.0

    def __init__(self, item):
        self.pos = Point(item.get('X'), item.get('Y'))
        self.mass = item.get('M')
        self.id = item.get('Id')

    def __str__(self):
        return 'id: {}, pos: {}, mass: {}, radius: {}'.format(self.id, str(self.pos), self.mass, self.radius)
