from collections import defaultdict
import heapq as heap

input_text = open('15_input').read().splitlines()


def tiled_grid(text, repeat_count):
    vertex_grid = defaultdict(lambda: defaultdict(lambda: float('inf')))
    cost_grid = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for row_i, row_val in enumerate(text):
        for col_i, col_val in enumerate(row_val):
            for horiz in range(repeat_count):
                for vert in range(repeat_count):
                    risk_incr = horiz + vert
                    horiz_shift = horiz * 100
                    vert_shift = vert * 100
                    cost_val = int(col_val)
                    if cost_val + risk_incr > 9:
                        cost_val = (cost_val + risk_incr) % 10 + 1
                    else:
                        cost_val += risk_incr
                    vertex_grid[row_i + vert_shift][col_i + horiz_shift] = int(cost_val)
                    cost_grid[row_i + vert_shift][col_i + horiz_shift] = float('inf')
    return vertex_grid, cost_grid


def dijkstra_cost_from(start_row, start_col, vertex_grid, cost_grid):
    visited = set()
    pq = []
    cost_grid[start_row][start_col] = 0
    heap.heappush(pq, (0, start_row, start_col))

    while pq:
        _, cur_row, cur_col = heap.heappop(pq)
        visited.add((cur_row, cur_col))
        cur_cost = cost_grid[cur_row][cur_col]

        #up
        if (cur_row - 1, cur_col) not in visited:
            new_cost = cur_cost + vertex_grid[cur_row - 1][cur_col]
            if cost_grid[cur_row - 1][cur_col] > new_cost:
                cost_grid[cur_row - 1][cur_col] = new_cost
                heap.heappush(pq, (new_cost, cur_row - 1, cur_col))
        #down
        if (cur_row + 1, cur_col) not in visited:
            new_cost = cur_cost + vertex_grid[cur_row + 1][cur_col]
            if cost_grid[cur_row + 1][cur_col] > new_cost:
                cost_grid[cur_row + 1][cur_col] = new_cost
                heap.heappush(pq, (new_cost, cur_row + 1, cur_col))
        #left
        if (cur_row, cur_col - 1) not in visited:
            new_cost = cur_cost + vertex_grid[cur_row][cur_col - 1]
            if cost_grid[cur_row][cur_col - 1] > new_cost:
                cost_grid[cur_row][cur_col - 1] = new_cost
                heap.heappush(pq, (new_cost, cur_row, cur_col - 1))
        #up
        if (cur_row, cur_col + 1) not in visited:
            new_cost = cur_cost + vertex_grid[cur_row][cur_col + 1]
            if cost_grid[cur_row][cur_col + 1] > new_cost:
                cost_grid[cur_row][cur_col + 1] = new_cost
                heap.heappush(pq, (new_cost, cur_row, cur_col + 1))

    return cost_grid


print("Part 1: ", dijkstra_cost_from(0, 0, *tiled_grid(input_text, 1))[99][99])
print("Part 2: ", dijkstra_cost_from(0, 0, *tiled_grid(input_text, 5))[499][499])
