from unittest import TestCase
from mars_rover import MarsRover


class TestMarsRover(TestCase):
    def setUp(self):
        self.rover = MarsRover()

    def test_init_position(self):
        self.assertEquals(self.rover.get_position(), (0, 0, 'N'))

    def test_move_forward_from_init_pos(self):
        self.rover.move('f')
        self.assertEquals(self.rover.get_position(), (0, 1, 'N'))

    def test_rotate_right_from_init_pos(self):
        self.rover.move('r')
        self.assertEquals(self.rover.get_position(), (0, 0, 'E'))

    def test_rotate_right_twice_from_init_pos(self):
        self.rover.move('r')
        self.rover.move('r')
        self.assertEquals(self.rover.get_position(), (0, 0, 'S'))

    def test_rotate_three_times_from_init_pos(self):
        self.rover.move('r')
        self.rover.move('r')
        self.rover.move('r')
        self.assertEquals(self.rover.get_position(), (0, 0, 'W'))

    def test_rotate_four_times_from_init_pos(self):
        self.rover.move('r')
        self.rover.move('r')
        self.rover.move('r')
        self.rover.move('r')
        self.assertEquals(self.rover.get_position(), (0, 0, 'N'))

    def test_rotate_left_from_init_pos(self):
        self.rover.move('l')
        self.assertEquals(self.rover.get_position(), (0, 0, 'W'))

    def test_rotate_left_and_then_move_forward(self):
        self.rover.move('l')
        self.rover.move('f')
        self.assertEquals(self.rover.get_position(), (-1, 0, 'W'))

    def test_rotate_left_five_times_from_init_pos(self):
        self.rover.move('l')
        self.rover.move('l')
        self.rover.move('l')
        self.rover.move('l')
        self.rover.move('l')
        self.assertEquals(self.rover.get_position(), (0, 0, 'W'))

    def test_rover_accepts_multiple_commands(self):
        self.rover.move('rr')
        self.assertEquals(self.rover.get_position(), (0, 0, 'S'))

    def test_move_forward_facing_east(self):
        self.rover.move('r')

        self.rover.move('f')

        self.assertEquals(self.rover.get_position(), (1, 0, 'E'))
