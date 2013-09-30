from unittest import TestCase
from mars_rover import (
    MarsRover,
    Point,
    NORTH,
    SOUTH,
    EAST,
    WEST,
)


class TestMarsRover(TestCase):
    def test_accepts_initial_point(self):
        initial_position = Point(0, 0)

        rover = MarsRover(initial_position, None)

        self.assertEquals(rover.position, initial_position)

    def test_accepts_initial_direction(self):
        rover = MarsRover(None, NORTH)

        self.assertIs(rover.direction, NORTH)

    def test_move_forward_to_the_north_increments_y_axis(self):
        rover = MarsRover(Point(0, 0), NORTH)

        rover.move_forward()

        self.assertEquals(rover.position, Point(0, 1))

    def test_move_forward_to_the_east_increments_x_axis(self):
        rover = MarsRover(Point(0, 0), EAST)

        rover.move_forward()

        self.assertEquals(rover.position, Point(1, 0))

    def test_move_forward_to_the_south_decrements_y_axis(self):
        rover = MarsRover(Point(0, 0), SOUTH)

        rover.move_forward()

        self.assertEquals(rover.position, Point(0, -1))

    def test_move_forward_to_the_west_decrements_x_axis(self):
        rover = MarsRover(Point(0, 0), WEST)

        rover.move_forward()

        self.assertEquals(rover.position, Point(-1, 0))

    def test_move_backward_to_the_north_decrements_y_axis(self):
        rover = MarsRover(Point(0, 0), NORTH)

        rover.move_backward()

        self.assertEquals(rover.position, Point(0, -1))

    def test_turn_to_the_right_from_north_sets_direction_to_east(self):
        rover = MarsRover(None, NORTH)

        rover.turn_right()

        self.assertEquals(rover.direction, EAST)

    def test_turn_to_the_right_from_east_sets_direction_to_south(self):
        rover = MarsRover(None, EAST)

        rover.turn_right()

        self.assertEquals(rover.direction, SOUTH)

    def test_turn_to_the_right_from_south_sets_direction_to_west(self):
        rover = MarsRover(None, SOUTH)

        rover.turn_right()

        self.assertEquals(rover.direction, WEST)

    def test_turn_to_the_right_from_west_sets_direction_to_north(self):
        rover = MarsRover(None, WEST)

        rover.turn_right()

        self.assertEquals(rover.direction, NORTH)

    def test_turn_to_the_left_from_north_sets_direction_to_west(self):
        rover = MarsRover(None, NORTH)

        rover.turn_left()

        self.assertEquals(rover.direction, WEST)

    def test_wraps_when_forward_and_north_limit_reached(self):
        rover = MarsRover(Point(0, 10), NORTH)

        rover.move_forward()

        self.assertEquals(rover.position, Point(0, 0))
