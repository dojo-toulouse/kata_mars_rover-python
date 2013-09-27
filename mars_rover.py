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


class MarsRover(object):
    def __init__(self, initial_position, initial_direction):
        self._position = initial_position
        self._direction = initial_direction

    @property
    def position(self):
        return self._position

    @property
    def direction(self):
        return self._direction

    def forward(self):
        if self.direction == 'N':
            self._position = (self.position[0], self.position[1] + 1)
        elif self.direction == 'E':
            self._position = (self.position[0] + 1, self.position[1])
        elif self.direction == 'S':
            self._position = (self.position[0], self.position[1] - 1)
        elif self.direction == 'W':
            self._position = (self.position[0] - 1, self.position[1])
