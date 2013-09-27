from unittest import TestCase
from mars_rover import MarsRover


class TestMarsRover(TestCase):
    def test_accepts_initial_point(self):
        initial_position = (0, 0)

        rover = MarsRover(initial_position, None)

        self.assertEquals(rover.position, initial_position)

    def test_accepts_initial_direction(self):
        initial_direction = 'N'

        rover = MarsRover(None, initial_direction)

        self.assertEquals(rover.direction, initial_direction)
