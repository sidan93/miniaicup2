from collections import namedtuple
from objects.food import Food


World = namedtuple('World', 'width height food_mass')


def get_world_info(world):
    world = World(
        world.get('GAME_WIDTH'),
        world.get('GAME_HEIGHT'),
        world.get('FOOD_MASS')
    )

    Food.food = world.food_mass

    return world
