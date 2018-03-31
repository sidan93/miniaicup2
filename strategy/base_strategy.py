import json
from objects.player import Me, Opponent
from strategy.parse_tick import parse_tick, Tick
from libs.utils import *


class BaseStrategy:
    def __init__(self, world):
        self.world = world
        self.me = Me(1)
        self.opps = {}
        self.tick = 0

    def run(self):
        while True:
            try:
                tick = parse_tick(json.loads(input()))
                self.set_pl(tick)
                cmd = self.on_tick(tick)
                self.tick += 1
                print(json.dumps(cmd))
            except:
                import traceback
                msg = traceback.format_exc()
                debug(msg)
                raise

    def set_pl(self, t: Tick):
        self.me.update(t.me)

        self.opps = {}
        for key, item in t.opponents.items():
            opp = Opponent(key)
            opp.update(item)
            self.opps[key] = opp

    def on_tick(self, t: Tick):
        raise NotImplementedError()
