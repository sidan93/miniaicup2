import json
from objects.player import Me, Opponent
from strategy.parse_tick import parse_tick, Tick
from libs.utils import *


class BaseStrategy:
    def __init__(self, world):
        self.world = world
        self.me = Me(1)
        self.opp2 = Opponent(2)
        self.opp3 = Opponent(3)
        self.opp4 = Opponent(4)
        self.opps = [self.opp2, self.opp3, self.opp4]
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

        self.opp2.update(t.opponents.get('2'))
        self.opp3.update(t.opponents.get('3'))
        self.opp4.update(t.opponents.get('4'))

    def on_tick(self, t: Tick):
        raise NotImplementedError()
