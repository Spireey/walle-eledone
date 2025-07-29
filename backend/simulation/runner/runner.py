from .grid import Grid
from .robot import Robot

class Runner:
    def __init__(self, robot_count=5, trash_count=50):
        self.grid = Grid()
        self.robots = []
        self.turn = 0

        for i in range(robot_count):
            x, y = self.grid.get_random_empty_cell()
            self.grid.cells[y][x].robot_id = i
            self.robots.append(Robot(i, x, y))

        for _ in range(trash_count):
            x, y = self.grid.get_random_empty_cell()
            self.grid.cells[y][x].has_trash = True

    def step(self):
        for robot in self.robots:
            robot.act(self.grid)
        self.turn += 1

    def get_state(self):
        return {
            "turn": self.turn,
            "robots": [{"id": r.id, "x": r.x, "y": r.y, "carrying": r.carrying} for r in self.robots],
            "base": self.grid.base,
            "trash": [
                {"x": x, "y": y}
                for y, row in enumerate(self.grid.cells)
                for x, cell in enumerate(row)
                if cell.has_trash
            ]
        }
