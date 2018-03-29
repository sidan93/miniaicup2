import json

from libs.game import get_world_info
from objects.food import Food


class Strategy:
    def __init__(self):
        self.config = None
        self.game = None

    def run(self):
        self.config = json.loads('{}')
        self.game = get_world_info(self.config)

        while True:
            tick = parse_tick(json.loads('{}'))


def parse_tick(data):
    result = {
        'players': [],
        'food': [],
        'virus': [],
        'ejection': []
    }

    for item in data.get('Objects'):
        if item.get('F'):
            result['food'].append(Food(item))

    return result
