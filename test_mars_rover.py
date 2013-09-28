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

    def test_move_forward_to_the_north_increments_y_axis(self):
        rover = MarsRover((0, 0), 'N')

        rover.forward()

        self.assertEquals(rover.position, (0, 1))

    def test_move_forward_to_the_east_increments_x_axis(self):
        rover = MarsRover((0, 0), 'E')

        rover.forward()

        self.assertEquals(rover.position, (1, 0))

    def test_move_forward_to_the_south_decrements_y_axis(self):
        rover = MarsRover((0, 0), 'S')

        rover.forward()

        self.assertEquals(rover.position, (0, -1))

    def test_move_forward_to_the_west_decrements_x_axis(self):
        rover = MarsRover((0, 0), 'W')

        rover.forward()

        self.assertEquals(rover.position, (-1, 0))

    def test_move_backward_to_the_north_decrements_y_axis(self):
        rover = MarsRover((0, 0), 'N')

        rover.backward()

        self.assertEquals(rover.position, (0, -1))
