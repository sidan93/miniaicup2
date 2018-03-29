import random

from libs.point import Point
from libs.vector import Vector

from libs.utils import *
from libs.game import World


class Part:
    def __init__(self, data):
        cur_fr = data
        self.id = cur_fr.get('Id')
        self.pos = Point(cur_fr.get('X'), cur_fr.get('Y'))
        self.radius = cur_fr.get('R')
        self.mass = cur_fr.get('M')
        self.speed = Vector(cur_fr.get('SX'), cur_fr.get('SY'))

    def update(self, part):
        self.pos = part.pos
        self.radius = part.radius
        self.mass = part.mass
        self.speed = part.speed


class Player:
    def __init__(self, id_: int):
        self.id = str(id_)
        self.parts = {}
        self.head = None

    def update(self, data: list):
        self.parts = {}
        self.head = None

        for item in (data or []):
            id_, pid = self.get_id(item.get('Id'))

            self.parts[pid] = Part(item)
            if self.head is None:
                self.head = pid
            else:
                if self.parts[self.head].mass < self.parts[pid].mass:
                    self.head = pid

    @staticmethod
    def get_id(data: str):
        if data.find('.') != -1:
            spl = data.split('.')
            return spl[0], spl[1]
        return data, '0'


class Me(Player):
    def __init__(self, id_: int):
        super().__init__(id_)

        self.last_target = None

    @property
    def mass(self):
        return self.parts[self.head].mass

    @property
    def pos(self):
        return self.parts[self.head].pos

    @property
    def radius(self):
        return self.parts[self.head].radius

    def get_target(self, world: World, tick: int):
        center_x = world.width / 2
        center_y = world.height / 2
        if self.last_target is None:
            self.last_target = (Point(center_x + random.uniform(-1, 1) * center_x, center_y + random.uniform(-1, 1) * center_y), tick)
        else:
            if tick - self.last_target[1] > 50:
                self.last_target = (Point(center_x + random.uniform(-1, 1) * center_x, center_y + random.uniform(-1, 1) * center_y), tick)

        return self.last_target[0]

class Opponent(Player):
    pass

