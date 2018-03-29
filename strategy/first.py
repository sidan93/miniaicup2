import random
import math
from collections import namedtuple

from libs.utils import *
from libs.point import *
from libs.vector import *

from strategy.base_strategy import BaseStrategy
from strategy.parse_tick import Tick


Target = namedtuple('Target', 'type pos dist mass value')


class ETarget:
    Null = 0
    Food = 1
    Opp = 2


class StrFirst(BaseStrategy):
    def on_tick(self, t: Tick):

        # To что съедобно
        food_list = []

        # То чего мы боимся
        warn_all_list = t.virus

        # food * 1.2 < my_mass
        max_mass = self.me.mass / 1.2
        for opp in self.opps:
            for part in opp.parts.values():
                if part.mass > max_mass:
                    continue

                # if part.mass / 1.2 > self.me.mass:
                #    warn_all_list.append(part)

                food_list.append(Target(ETarget.Opp, part.pos, dist(part.pos, self.me.pos), part.mass, part.mass))

        for food in t.food:
            food_list.append(Target(ETarget.Food, food.pos, dist(food.pos, self.me.pos), food.mass, food.mass))

        warn_list = []  # (Vector, Warn)
        for warn in warn_all_list:
            if dist(self.me.pos, warn.pos) < self.me.radius * 2:
                warn_list.append((Vector.from_p(self.me.pos, warn.pos), warn))

        # Значение к которому надо если что идти
        food_list.append(Target(ETarget.Null, self.me.get_target(self.world, self.tick), 0, 0, 0))

        target = None
        for food in food_list:
            # Найдем самую вкусную
            cur_v = Vector.from_p(self.me.pos, food.pos)
            value = 1
            for warn in warn_list:
                angle = get_angle(cur_v, warn[0])
                angle = math.copysign(angle, 1)
                debug(angle)
                debug(str(food.pos) + str(cur_v))
                debug(str(warn[1].id) + str(warn[1].pos) + str(warn[0]))

                if angle < 45:
                    value = 0

            if value <= 0 and food.type != ETarget.Null:
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

        return r(self.me.get_target(self.world, self.tick), 'random')

