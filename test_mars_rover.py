from unittest import TestCase
from mars_rover import MarsRover


class TestMarsRover(TestCase):
    def test_accepts_initial_point(self):
        initial_position = (0, 0)

        rover = MarsRover(initial_position)

        self.assertEquals(rover.position, initial_position)
