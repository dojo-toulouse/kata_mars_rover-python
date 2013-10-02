"""
Develop an api that moves a rover around on a grid.

You are given the initial starting point (x,y) of a rover
and the direction (N,S,E,W) it is facing.

The rover receives a character array of commands.

Implement commands that move the rover forward/backward (f,b).

Implement commands that turn the rover left/right (l,r).

Implement wrapping from one edge of the grid to another.
(planets are spheres after all)

Implement obstacle detection before each move to a new square.
If a given sequence of commands encounters an obstacle,
the rover moves up to the last possible point and reports the obstacle.
"""
from operator import add, sub


class Point(tuple):
    def __new__(cls, *coords):
        return tuple.__new__(cls, coords)

    def _operation(self, operator, other):
        values_by_axis = zip(self, other)
        result = map(lambda a: operator(*a), values_by_axis)
        return Point(*result)

    def __add__(self, other):
        return self._operation(add, other)

    def __sub__(self, other):
        return self._operation(sub, other)


class Direction(Point):
    def __new__(cls, *coords):
        return Point.__new__(cls, *coords)


NORTH = Direction(0, 1)
SOUTH = Direction(0, -1)
EAST = Direction(1, 0)
WEST = Direction(-1, 0)

TO_THE_LEFT = -1
TO_THE_RIGHT = 1


class Grid(object):
    _directions = (
        NORTH,
        EAST,
        SOUTH,
        WEST
    )

    def __init__(self, position=Point(0, 0), direction=NORTH, size=(10, 10)):
        self._position = position
        self.direction = direction
        self._size = size

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if value[1] >= self._size[1]:
            self._position = Point(value[0], 0)
        elif value[1] < 0:
            self._position = Point(value[0], self._size[1])
        elif value[0] >= self._size[0]:
            self._position = Point(0, value[1])
        elif value[0] < 0:
            self._position = Point(self._size[0], value[1])
        else:
            self._position = value

    def _get_direction(self, start, where):
        index = self._directions.index(start) + where
        index %= 4
        return self._directions[index]

    def left_direction(self):
        return self._get_direction(self.direction, TO_THE_LEFT)

    def right_direction(self):
        return self._get_direction(self.direction, TO_THE_RIGHT)


class MarsRover(object):
    _commands_map = {
        'l': 'turn_left',
        'r': 'turn_right',
        'f': 'move_forward',
        'b': 'move_backward',
    }

    def __init__(self, initial_position, initial_direction, size=(10, 10)):
        self._grid = Grid(initial_position, initial_direction, size)

    @property
    def position(self):
        return self._grid.position

    @property
    def direction(self):
        return self._grid.direction

    def move_forward(self):
        self._grid.position += self._grid.direction

    def move_backward(self):
        self._grid.position -= self._grid.direction

    def turn_left(self):
        self._grid.direction = self._grid.left_direction()

    def turn_right(self):
        self._grid.direction = self._grid.right_direction()

    def _call(self, command):
        handler = getattr(self, self._commands_map[command])
        handler()

    def move(self, commands):
        for command in commands:
            self._call(command)
