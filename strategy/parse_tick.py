from libs.utils import *

from collections import namedtuple

from objects.food import Food
from objects.player import Player
from objects.virus import Virus

Tick = namedtuple('Tick', 'me opponents food virus ejection')


def parse_tick(data: dict) -> Tick:
    me = data.get('Mine')

    food = []
    virus = {}
    opponents = {}
    for item in data.get('Objects'):
        type_ = item.get('T')
        if type_ == 'F':
            food.append(Food(item))

        if type_ == 'P':
            id_, pid = Player.get_id(item.get('Id'))
            opponents.setdefault(id_, []).append(item)

        if type_ == 'V':
            id_ = item.get('Id')
            virus[id_] = Virus(item)

    return Tick(me, opponents, food, virus, None)
