import random
import math
from collections import namedtuple

from libs.utils import *
from libs.point import *
from libs.vector import *

from strategy.base_strategy import BaseStrategy
from strategy.parse_tick import Tick


Target = namedtuple('Target', 'type pos dist mass value')
Warn = namedtuple('Warn', 'warn vec angle')


class ETarget:
    Null = 0
    Food = 1
    Opp = 2


class StrFirst(BaseStrategy):
    def __init__(self):
        super().__init__()

        self.bad_food = {}

    def on_tick(self, t: Tick):

        # To что съедобно
        food_list = []

        # То чего мы боимся
        warn_all_list = list(t.virus.values())

        # Удали плохую еду, которая старая
        #for key, tick in self.bad_food:
        #    if self.tick - tick > 100:
        #        self.bad_food.pop(key)

        # food * 1.2 < my_mass
        max_mass = self.me.mass / 1.2
        for opp in self.opps.values():
            for part in opp.parts.values():
                if part.mass / 1.2 > self.me.mass:
                    warn_all_list.append(part)

                if part.mass > max_mass:
                    continue

                food_list.append(Target(ETarget.Opp, part.pos, dist(part.pos, self.me.pos), part.mass, part.mass))

        for food in t.food:
            # Если еда была плохой, не идем к ней
            if (food.pos.x, food.pos.y) in self.bad_food:
                continue

            # Не таскаем еду с границ
            if food.pos.x < self.me.radius or food.pos.x > self.world.width - self.me.radius:
                continue
            if food.pos.y < self.me.radius or food.pos.y > self.world.height - self.me.radius:
                continue
            food_list.append(Target(ETarget.Food, food.pos, dist(food.pos, self.me.pos), food.mass, food.mass))

        warn_list = []  # [Warn]
        for warn in warn_all_list:
            if dist(self.me.pos, warn.pos) < self.me.radius * 4:
                warn_vec = Vector.from_p(self.me.pos, warn.pos)
                warn_angle = get_angle(Vector.up(), warn_vec.normalize())
                warn_list.append(Warn(warn, warn_vec, warn_angle))

        # Значение к которому надо если что идти
        food_list.append(Target(ETarget.Null, self.me.get_target(self.world, self.tick), 0, 0, 0))

        target = None
        warn_angle = 30
        for food in food_list:
            # Найдем самую вкусную
            food_vec = Vector.from_p(self.me.pos, food.pos)
            food_angle = get_angle(Vector.up(), food_vec.normalize())

            value = 1
            for warn in warn_list:
                if in_angle(warn.angle, warn_angle, food_angle):
                    value = 0

            if value <= 0:
                self.bad_food[(food.pos.x, food.pos.y)] = self.tick
                continue

            # TODO Надо учитывать направление движения
            if target is None:
                target = food
            else:
                if target.value < food.value:
                    target = food
                elif target.value == food.value:
                    if target.dist > food.dist:
                        target = food

        if target:
            return r(target.pos, 'attack')

        return r(self.me.pos, 'random')

