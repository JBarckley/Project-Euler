# Every Path will have the same number of moves
from itertools import islice

def lattice_paths(n):
    grid = [[0 for i in range(n)] for j in range(n - 1)]
    grid.insert(0, [1 for k in range(n)])
    for m in range(n):
        grid[m][0] = 1
    print_lattice(create_pathway_diagram(1, n, grid))



def create_pathway_diagram(st, n, grid):
    if st < n:
        grid[st][st] = grid[st - 1][st] * 2
        for k in range(st + 1, n):
            grid[st][k] = grid[st][k - 1] + grid[st - 1][k]
        return create_pathway_diagram(st + 1, n, grid)
    else:
        grid[n - 1][n - 1] = grid[n - 2][n - 1] * 2
        return grid


def print_lattice(grid):
    for i in range(0, len(grid)):
        print(grid[i])




lattice_paths(501)
