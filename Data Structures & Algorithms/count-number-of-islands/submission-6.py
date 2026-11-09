class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def sink_island(x, y):
            # form a stack of what to visit, keep visiting until we have no more to visit
            # turn each spot to 0 as soon as we add it, so nothing gets added twice
            grid[x][y] = "0"
            to_visit = [(x, y)]

            while to_visit:
                x, y = to_visit.pop()

                neighbors = [
                    (x - 1, y),  # up
                    (x + 1, y),  # down
                    (x, y - 1),  # left
                    (x, y + 1),  # right
                ]

                for nx, ny in neighbors:
                    in_bounds = 0 <= nx < ROWS and 0 <= ny < COLS
                    if in_bounds and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        to_visit.append((nx, ny))

        res = 0

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == "1":
                    res += 1
                    sink_island(x, y)

        return res