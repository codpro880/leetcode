"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
import numpy as np
class Node(object):
    def __init__(self, val):
        self.adj_nodes = []
        self.val = val

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        grid = self._create_char_lists(grid)
        array_of_nodes = self._create_grid_of_nodes(grid)

        any_nonzero = len([x for x in array_of_nodes.reshape(-1) if x.val == 1])
        num_islands = 0
        while any_nonzero:
            array_of_nodes = self._remove_next_island_chain(array_of_nodes)
            any_nonzero = len([x for x in array_of_nodes.reshape(-1) if x.val == 1])
            num_islands += 1
        return num_islands

    def _create_char_lists(self, grid):
        result = []
        for row in grid:
            if len(row) == 1:
                result.append([int(x) for x in row[0]])
            else:
                result.append([int(x) for x in row])
        return result

    def _create_grid_of_nodes(self, grid):
        nodes = []
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                node = Node(grid[i][j])
                row.append(node)
            nodes.append(row)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                adj_nodes = self._get_adj_nodes(nodes, i, j)
                node = nodes[i][j]
                node.adj_nodes = adj_nodes
        return np.array(nodes)

    def _get_adj_nodes(self, nodes, i, j):
        adj = []
        try:
            if i-1 >= 0:
                top = nodes[i-1][j]
                adj.append(top)
        except IndexError:
            pass
        try:
            if j-1 >= 0:
                left = nodes[i][j-1]
                adj.append(left)
        except IndexError:
            pass
        try:
            right = nodes[i][j+1]
            adj.append(right)
        except IndexError:
            pass
        try:
            bottom = nodes[i+1][j]
            adj.append(bottom)
        except IndexError:
            pass
        return adj

    def _remove_next_island_chain(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].val == 1:
                    self._mark_all_adj_land_water(grid[i][j])
                    return grid

    def _mark_all_adj_land_water(self, node):
        if node.val == 0:
            return
        node.val = 0
        land_adj = [adj for adj in node.adj_nodes if adj.val == 1]
        for adj in land_adj:
            self._mark_all_adj_land_water(adj)

    def _pretty_print_grid(self, grid):
        arr = [[x.val for x in y] for y in grid]
        for line in arr:
            print(line)
        

if __name__ == "__main__":
    sol = Solution()
    grid = [["11110"],
            ["11010"],
            ["11000"],
            ["00000"]]
    num_islands = sol.numIslands(grid)
    assert num_islands == 1

    grid = [["11000"],
            ["11000"],
            ["00100"],
            ["00011"]]
    num_islands = sol.numIslands(grid)
    print(num_islands)
    assert num_islands == 3
