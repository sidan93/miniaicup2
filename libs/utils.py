from libs.point import Point


__all__ = ['debug', 'r']


def debug(message):
    file = open('D:\Project\miniaicup2\log.txt', 'a')
    file.write('\n' + str(message))
    file.close()


def r(pos: Point, message: str) -> dict:
    return {
        'X': pos.x,
        'Y': pos.y,
        'Debug': message or ''
    }