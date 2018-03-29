import json

from libs.game import get_world_info
from strategy.first import StrFirst


config = json.loads(input())
world = get_world_info(config)

if __name__ == '__main__':
    StrFirst(world).run()
