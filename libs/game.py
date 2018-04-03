from collections import namedtuple
from objects.food import Food
from objects.virus import Virus


World = namedtuple('World', 'data width height food_mass virus_radius')


def get_world_info(world) -> World:
    world = World(
        world,
        world.get('GAME_WIDTH'),
        world.get('GAME_HEIGHT'),
        world.get('FOOD_MASS'),
        world.get('VIRUS_RADIUS'),
    )

    Food.mass = world.food_mass
    Virus.radius = world.virus_radius

    return world
