from unittest import TestCase
from mars_rover import MarsRover, Point, Direction


class TestMarsRover(TestCase):
    def test_accepts_initial_point(self):
        initial_position = Point(0, 0)

        rover = MarsRover(initial_position, None)

        self.assertEquals(rover.position, initial_position)

    def test_accepts_initial_direction(self):
        initial_direction = Direction('N')

        rover = MarsRover(None, initial_direction)

        self.assertEquals(rover.direction, initial_direction)

    def test_move_forward_to_the_north_increments_y_axis(self):
        rover = MarsRover(Point(0, 0), Direction('N'))

        rover.move_forward()

        self.assertEquals(rover.position, Point(0, 1))

    def test_move_forward_to_the_east_increments_x_axis(self):
        rover = MarsRover(Point(0, 0), Direction('E'))

        rover.move_forward()

        self.assertEquals(rover.position, Point(1, 0))

    def test_move_forward_to_the_south_decrements_y_axis(self):
        rover = MarsRover(Point(0, 0), Direction('S'))

        rover.move_forward()

        self.assertEquals(rover.position, Point(0, -1))

    def test_move_forward_to_the_west_decrements_x_axis(self):
        rover = MarsRover(Point(0, 0), Direction('W'))

        rover.move_forward()

        self.assertEquals(rover.position, Point(-1, 0))

    def test_move_backward_to_the_north_decrements_y_axis(self):
        rover = MarsRover(Point(0, 0), Direction('N'))

        rover.move_backward()

        self.assertEquals(rover.position, Point(0, -1))

    def test_turn_to_the_left_from_north_sets_direction_to_east(self):
        rover = MarsRover(None, Direction('N'))

        rover.turn_left()

        self.assertEquals(rover.direction, Direction('E'))

    def test_turn_to_the_left_from_east_sets_direction_to_south(self):
        rover = MarsRover(None, Direction('E'))

        rover.turn_left()

        self.assertEquals(rover.direction, Direction('S'))

    def test_turn_to_the_left_from_south_sets_direction_to_west(self):
        rover = MarsRover(None, Direction('S'))

        rover.turn_left()

        self.assertEquals(rover.direction, Direction('W'))

    def test_turn_to_the_left_from_west_sets_direction_to_north(self):
        rover = MarsRover(None, Direction('W'))

        rover.turn_left()

        self.assertEquals(rover.direction, Direction('N'))
