from unittest import TestCase
from mars_rover import MarsRover


class TestMarsRover(TestCase):
    def setUp(self):
        self.rover = MarsRover()

    def test_exemple(self):
        self.assertIsInstance(self.rover, MarsRover)
