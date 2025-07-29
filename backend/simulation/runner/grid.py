import random

class Cell:
    def __init__(self):
        self.has_trash = False
        self.robot_id = None

class Grid:
    def __init__(self, base_pos=(0, 0)):
        self.size = 32
        self.cells = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self.base = base_pos

    def in_bounds(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def get_random_empty_cell(self):
        while True:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (x, y) != self.base and not self.cells[y][x].has_trash:
                return x, y