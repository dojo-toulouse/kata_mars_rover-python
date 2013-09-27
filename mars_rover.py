class MarsRover(object):

    cardinal_points = ["N", "E", "S", "W"]

    def __init__(self):
        self.cardinal_point_index = 0
        self.x = 0
        self.y = 0

    def get_position(self):
        return (self.x,
                self.y,
                self.cardinal_points[self.cardinal_point_index])

    def move(self, commands):
        for command in commands:
            self.execute(command)

    def execute(self, command):
        if command == 'f':
            self.move_forward()
        elif command == 'r':
            self.turn_right()
        elif command == 'l':
            self.turn_left()

    def move_forward(self):
        if self.is_facing_north():
            self.y += 1
        elif self.is_facing_east():
            self.x += 1
        else:
            self.x -= 1

    def is_facing_north(self):
        return self.is_facing('N')

    def is_facing_east(self):
        return self.is_facing('E')

    def is_facing(self, direction):
        return self.cardinal_points.index(direction) == self.cardinal_point_index

    def turn(self, increment):
        self.cardinal_point_index += increment
        self.cardinal_point_index %= len(self.cardinal_points)

    def turn_right(self):
        self.turn(1)

    def turn_left(self):
        self.turn(-1)
