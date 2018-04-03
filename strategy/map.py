from libs.game import World
from libs.point import Point
from libs.vector import Vector
from objects.virus import Virus
from libs.utils import debug


#
# Карта с полями
# Поля по умолчанию имеют значение = 10
# Чем выше значение чем больше хочется боту идти туда
# Значения интовые
# от -100 до 10
# Каждый вирус уменьшает значение вокруг себя по нисходящей с радиусом вируса * 3
# Когда вирус теряется, значит его съели, ценность того места выростает, т.к. там может быть разделенный враг
#

#
# Градация значений по умолчанию
# + 50  когда пропадает вирус
# - 50  поле с вирусом
# - 100 поле с игроком которй больше меня
#
class Field:
    DEFAULT = 10
    VIRUS_CREATED = -50
    VIRUS_DESTR = 50

    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.value = Field.DEFAULT

    @property
    def pos(self):
        return Point(self.x*self.width, self.y*self.width)

    def __str__(self):
        return 'x: {}, y: {}, width: {}, value: {}'.format(self.x, self.y, self.width, self.value)


class Map:
    def __init__(self, world: World):
        self.world = world
        self.width_field = 20
        self.max_field = int(world.width / self.width_field)
        self.fields = [[Field(x, y, self.width_field) for y in range(1, self.max_field)] for x in range(1, self.max_field)]
        self.virus = {}

    def check_virus(self, virus: dict):
        new_keys = set(virus.keys())
        cur_keys = set(self.virus.keys())
        # Если ничего не изменилось, то ничего не делаем
        if cur_keys == new_keys:
            return True

        # Создадим новые вирусы
        for key in new_keys - cur_keys:
            self.add_virus(virus.get(key))

        # Удалим те, которые пропали
        for key in cur_keys - new_keys:
            self.delete_virus(self.virus.pop(key))

        self.to_log()

    def add_virus(self, virus: Virus):
        self.virus[virus.id] = virus
        self.set_gradient_value(virus.pos, virus.radius, virus.radius * 3, Field.VIRUS_CREATED, Field.DEFAULT)

    def delete_virus(self, virus: Virus):
        pass

    def set_gradient_value(self, pos: Point, min_radius: float, max_radius: float, min_value: int, max_value: int):
        field = self.get_field_by_pos(pos)
        min_radius_f = int(min_radius / self.width_field)
        max_radius_f = int(max_radius / self.width_field)

        # TODO пока что работаем квадратами, а не кругами
        left = field.x - max_radius_f if field.x - max_radius_f > 0 else 0
        right = field.x + max_radius_f if field.x + max_radius_f < self.max_field else self.max_field - 1
        top = field.y - max_radius_f if field.y - max_radius_f > 0 else 0
        bottom = field.y + max_radius_f if field.y + max_radius_f < self.max_field else self.max_field - 1

        left_min = field.x - min_radius_f if field.x - min_radius_f > 0 else 0
        right_min = field.x + min_radius_f if field.x + min_radius_f < self.max_field else self.max_field - 1
        top_min = field.y - min_radius_f if field.y - min_radius_f > 0 else 0
        bottom_min = field.y + min_radius_f if field.y + min_radius_f < self.max_field else self.max_field - 1

        for x in range(left, right):
            for y in range(top, bottom):
                cur_field = self.fields[x][y]
                # Если это минимальный круг
                if left_min < x < right_min and top_min < y < bottom_min:
                    cur_field.value = min_value
                    continue

                # Вычитаем градиент
                # Отношение текущий длинны к общей
                otn = Vector.from_p(pos, cur_field.pos).length() / max_radius
                # Ддлинна градиента
                all_grad = min_value - max_value
                # шаг отношения
                step = otn * all_grad

                cur_field.value = min(min_value - step, max_value)

    def get_field_by_pos(self, pos: Point):
        return self.fields[int(pos.x / self.width_field)][int(pos.y / self.width_field)]

    def to_log(self):
        def get_num(i):
            if 0 < i < 10:
                return '+0' + str(i)
            if -10 < i < 0:
                return '-0' + str(-i)
            if i < 0:
                return str(i)
            if i > 0:
                return '+' + str(i)
            if i == 0:
                return '+00'
            return str(i)
        debug('MAP')
        for x in range(0, self.max_field - 1):
            message = ''
            for y in range(0, self.max_field - 1):
                message += get_num(int(self.fields[x][y].value)) + ' '
            debug(message)

