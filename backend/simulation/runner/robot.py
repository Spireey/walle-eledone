import random

class Robot:
    def __init__(self, robot_id, x, y):
        self.id = robot_id
        self.x = x
        self.y = y
        self.carrying = False

    def act(self, grid):
        cell = grid.cells[self.y][self.x]

        if self.carrying and (self.x, self.y) == grid.base:
            self.carrying = False
            return "drop"

        if not self.carrying and cell.has_trash:
            cell.has_trash = False
            self.carrying = True
            return "pick-up"

        return self.move(grid)

    def move(self, grid):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if grid.in_bounds(nx, ny) and not grid.cells[ny][nx].robot_id:
                grid.cells[self.y][self.x].robot_id = None
                self.x, self.y = nx, ny
                grid.cells[self.y][self.x].robot_id = self.id
                return "move"
        return "wait"
