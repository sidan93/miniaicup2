import json
from libs.point import Point


__all__ = ['debug', 'r', 'Message', 'DEBUG_']


# Перед пзагрузской на сервис выставлять в false
DEBUG_ = False


def debug(message):
    if not DEBUG_:
        return
    # pc
    # file = open('D:\Project\miniaicup2\log.txt', 'a')
    # notebook
    file = open('F:\GITHUB\miniaicup2\log.txt', 'a')
    file.write('\n' + str(message))
    file.close()


class Message:
    def __init__(self):
        self.data = {}

    def add(self, action, message):
        self.data.setdefault(action, []).append(str(message))

    def clear(self):
        self.data = {}

    def __str__(self):
        result = ''
        for key, value_list in self.data.items():
            result += str(key) + ': ' + ', '.join(value_list) + '\n'
        return result


def r(pos: Point) -> dict:
    return {
        'X': pos.x,
        'Y': pos.y,
        'Debug': None
    }
