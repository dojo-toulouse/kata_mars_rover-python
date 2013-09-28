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


class Point(tuple):
    def __new__(cls, *coords):
        return tuple.__new__(cls, coords)

    def __add__(self, other):
        values_by_axis = zip(self, other)
        add_axis_value = lambda a: a[0] + a[1]
        result = map(add_axis_value, values_by_axis)
        return Point(*result)

    def __sub__(self, other):
        values_by_axis = zip(self, other)
        add_axis_value = lambda a: a[0] - a[1]
        result = map(add_axis_value, values_by_axis)
        return Point(*result)


class Direction(Point):
    def __new__(cls, *coords):
        return Point.__new__(cls, *coords)


NORTH = Direction(0, 1)
SOUTH = Direction(0, -1)
EAST = Direction(1, 0)
WEST = Direction(-1, 0)


class MarsRover(object):
    _directions = (
        NORTH,
        EAST,
        SOUTH,
        WEST
    )

    def __init__(self, initial_position, initial_direction):
        self._position = initial_position
        self._direction = initial_direction

    @property
    def position(self):
        return self._position

    @property
    def direction(self):
        return self._direction

    def move_forward(self):
        self._position += self.direction

    def move_backward(self):
        self._position -= self.direction

    def _left_of(self, direction):
        index = self._directions.index(direction) + 1
        index %= 4
        return self._directions[index]

    def turn_left(self):
        self._direction = self._left_of(self._direction)

    def _right_of(self, direction):
        index = self._directions.index(direction) - 1
        index %= 4
        return self._directions[index]

    def turn_right(self):
        self._direction = self._right_of(self._direction)
