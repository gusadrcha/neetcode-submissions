class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #    up: x - 1
        #  down: x + 1
        # right: y + 1
        #  left: y - 1

        # form a queue of what to visit, keep visiting until we have no more to visit

        def dfs(visited, queue, coord, grid):
            if coord in visited:
                if queue:
                    dfs(visited, queue, queue.pop(), grid)
                return

            x, y = coord
            visited.add(coord)
            
            # look up
            if x > 0 and grid[x - 1][y] == "1":
                queue.append((x - 1, y))
            # look down
            if x < len(grid) - 1 and grid[x + 1][y] == "1":
                queue.append((x + 1, y))
            # look left
            if y > 0 and grid[x][y - 1] == "1":
                queue.append((x, y - 1))
            # look right
            if y < len(grid[0]) - 1 and grid[x][y + 1] == "1":
                queue.append((x, y + 1))

            # turn current spot to 0
            grid[x][y] = "0"

            if not queue:
                return 
            
            nextCoord = queue.pop()

            dfs(visited, queue, (nextCoord[0], nextCoord[1]), grid)
        
        visited = set()

        ROW = len(grid)
        COL = len(grid[0])

        res = 0

        for x in range(ROW):
            for y in range(COL):
                if grid[x][y] == "1":
                    res += 1
                    dfs(visited, [], (x, y), grid)
        
        return res