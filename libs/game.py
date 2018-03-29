from collections import namedtuple
from objects.food import Food


World = namedtuple('World', 'data width height food_mass')


def get_world_info(world) -> World:
    world = World(
        world,
        world.get('GAME_WIDTH'),
        world.get('GAME_HEIGHT'),
        world.get('FOOD_MASS')
    )

    Food.mass = world.food_mass

    return world
