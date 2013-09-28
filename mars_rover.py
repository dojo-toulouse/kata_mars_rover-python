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


class MarsRover(object):
    directions = {
        'N': Point(0, 1),
        'S': Point(0, -1),
        'E': Point(1, 0),
        'W': Point(-1, 0),
    }

    def __init__(self, initial_position, initial_direction_name):
        self._position = initial_position
        self._direction_name = initial_direction_name

    @property
    def position(self):
        return self._position

    @property
    def direction_name(self):
        return self._direction_name

    def move_forward(self):
        direction = self.directions[self.direction_name]
        self._position += direction

    def move_backward(self):
        direction = self.directions[self.direction_name]
        self._position -= direction

    def turn_left(self):
        if self.direction_name == 'N':
            self._direction_name = 'E'
        elif self.direction_name == 'E':
            self._direction_name = 'S'
        elif self.direction_name == 'S':
            self._direction_name = 'W'
        else:
            self._direction_name = 'N'
