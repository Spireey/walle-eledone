from .grid import Grid
from .robot import Robot

class Runner:
    def __init__(self, robot_count=5, trash_count=50):
        self.grid = Grid()
        self.memory = []
        self.robots = []
        self.turn = 0
        self.score = 0

        for i in range(robot_count):
            x, y = self.grid.get_random_empty_cell()
            self.grid.cells[x][y].robot_id = i
            self.robots.append(Robot(i, x, y))

        for _ in range(trash_count):
            x, y = self.grid.get_random_empty_cell()
            self.grid.cells[x][y].has_trash = True

        for robot in self.robots:
            for dx in range(-5, 6):
                for dy in range(-5, 6):
                    x, y = robot.x + dx, robot.y + dy
                    if self.grid.in_bounds(x,y):
                        self.grid.cells[x][y].explored = True
                        if self.grid.cells[x][y].has_trash:
                            self.memory.append((x, y))

    def step(self):
        for robot in self.robots:
            robot.act(self, self.grid, self.memory)
        self.turn += 1

    def get_state(self):
        return {
            "turn": self.turn,
            "robots": [{"id": r.id, "x": r.x, "y": r.y, "carrying": r.carrying, "objective": r.objective} for r in self.robots],
            "grid": self.get_grid()["grid"],
            "memory": self.memory,
            "score": self.score,
        }

    def get_grid(self):
        grid = []
        for y in range(len(self.grid.cells)):
            grid.append([])
            for x in range(len(self.grid.cells[y])):
                if self.grid.cells[x][y].has_trash:
                    grid[y].append("trash")
                elif self.grid.cells[x][y].robot_id is not None:
                    grid[y].append("robot")
                else:
                    grid[y].append("empty")

        grid[0][0] = "base"
        return {"grid": grid}

    def get_visibility(self):
        grid = [["hidden" for _ in range(32)] for _ in range(32)]
        for y in range(32):
            for x in range(32):
                if self.grid.cells[x][y].explored:
                    grid[x][y] = "explored"
        return {"grid": grid}