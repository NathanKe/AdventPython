droplet_cubelets_text = open('18_input').read().splitlines()

cubelets = [tuple(map(int, x.split(","))) for x in droplet_cubelets_text]

surface_area = 0
unoccupied_neighbors = []
for cubelet in cubelets:
    top = (cubelet[0], cubelet[1], cubelet[2] + 1)
    bot = (cubelet[0], cubelet[1], cubelet[2] - 1)
    lef = (cubelet[0], cubelet[1] + 1, cubelet[2])
    rgh = (cubelet[0], cubelet[1] - 1, cubelet[2])
    fwd = (cubelet[0] + 1, cubelet[1], cubelet[2])
    bck = (cubelet[0] - 1, cubelet[1], cubelet[2])
    unoccupied_neighbors.extend([x for x in [top, bot, lef, rgh, fwd, bck] if x not in cubelets])

print("Part 1: ", len(unoccupied_neighbors))

# shitty dfs

# x_max = max(cubelets, key=lambda tu: tu[0])[0]
# y_max = max(cubelets, key=lambda tu: tu[1])[1]
# z_max = max(cubelets, key=lambda tu: tu[2])[2]
# overall_max = max(x_max, y_max, z_max) + 1

# def dist(ac, bc):
#     return abs(bc[0] - ac[0]) + abs(bc[1] - ac[1]) + abs(bc[2] - ac[2])

# trapped_cubelets = []

# def can_escape(ic, p=False):
#     paths = [[ic]]
#     while paths:
#         path = paths.pop()
#         if p:
#             print(path)
#         head = path[-1]
#         if max(head) >= overall_max or min(head) < 0:
#             return True
#         top = (head[0], head[1], head[2] + 1)
#         bot = (head[0], head[1], head[2] - 1)
#         lef = (head[0], head[1] + 1, head[2])
#         rgh = (head[0], head[1] - 1, head[2])
#         fwd = (head[0] + 1, head[1], head[2])
#         bck = (head[0] - 1, head[1], head[2])
#         neighbors = sorted([x for x in [top, bot, lef, rgh, fwd, bck] if x not in cubelets and x not in path],
#                            key=lambda tu: dist(ic, tu))
#         for neighbor in neighbors:
#             new_path = path[:]
#             new_path.append(neighbor)
#             paths.append(new_path)
#     return False
