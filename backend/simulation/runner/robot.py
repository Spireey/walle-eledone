import random

class Robot:
    def __init__(self, robot_id, x, y):
        self.id = robot_id
        self.x = x
        self.y = y
        self.carrying = False
        self.objective = None

    def act(self, runner, grid, memory):
        cell = grid.cells[self.x][self.y]

        # Drop if holding in base
        if self.carrying and (self.x, self.y) == grid.base:
            self.carrying = False
            return "drop"

        # Returning to base if holding trash
        if self.carrying:
            return self.return_to_base(runner, grid, memory)

        # Go to next trash
        if self.objective:
            return self.goto_objective(runner, grid, memory)

        # Pick up trash
        if not self.carrying and cell.has_trash:
            cell.has_trash = False
            self.carrying = True
            self.objective = None
            runner.emptied.append((self.x, self.y))
            return "pick-up"

        # Choose the next trash as objective
        if len(memory) != 0:
            self.objective = memory.pop(0)
            return self.goto_objective(runner, grid, memory)

        # Set an unexplored cell as objective
        to_explore = []
        for y in range(32):
            for x in range(32):
                if not grid.cells[x][y].explored:
                    to_explore.append((x, y))
        if len(to_explore) == 0:
            self.objective = (random.randint(16, 31), random.randint(16, 31))
        else:
            self.objective = random.choice(to_explore)
        return self.goto_objective(runner, grid, memory)

    def return_to_base(self, runner, grid, memory):
        if self.x > 0 and self.move(runner, grid, memory, (-1, 0)) == "move":
            return "move"
        if self.y > 0 and self.move(runner, grid, memory,  (0, -1)) == "move":
            return "move"
        return self.random_move(runner, grid, memory)


    def move(self, runner, grid, memory, direction):
        nx, ny = self.x + direction[0], self.y + direction[1]
        if grid.in_bounds(nx, ny) and not grid.cells[nx][ny].robot_id:
            grid.cells[self.x][self.y].robot_id = None
            if not grid.cells[self.x][self.y].has_trash:
                runner.emptied.append((self.x, self.y))

            self.x, self.y = nx, ny
            grid.cells[self.x][self.y].robot_id = self.id

            # Now that we moved, creating a list of new tiles to scout
            to_scout = []
            if direction == (-1, 0): # Left
                to_scout = [(nx - 5, ny + dy) for dy in range(-5, 6)]
            elif direction == (1, 0):
                to_scout = [(nx + 5, ny + dy) for dy in range(-5, 6)]
            elif direction == (0, -1):
                to_scout = [(nx + dx, ny - 5) for dx in range(-5, 6)]
            elif direction == (0, 1):
                to_scout = [(nx + dx, ny + 5) for dx in range(-5, 6)]

            for x, y in to_scout:
                if grid.in_bounds(x,y) and not grid.cells[x][y].explored:
                    grid.cells[x][y].explored = True
                    if grid.cells[x][y].has_trash:
                        memory.append((x, y))
            return "move"
        return "wait"

    def random_move(self, runner, grid, memory):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            if self.move(runner, grid, memory, (dx, dy)) == "move":
                return "move"
        return "wait"

    def goto_objective(self, runner, grid, memory):
        x, y = self.objective
        if self.x != x:
            direction = (1 if self.x < x else -1, 0)
            return self.move(runner, grid, memory, direction)
        if self.y != y:
            direction = (0, 1 if self.y < y else -1)
            return self.move(runner, grid, memory, direction)
        self.objective = None
        return "wait"