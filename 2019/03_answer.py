import re

input_wires = open('03_input').read().splitlines()


def wire_trace(wire_str):
    wire_steps = wire_str.split(",")
    x = 0
    y = 0
    step_count = 0
    out = []
    for st in wire_steps:
        dr, cn = re.match(r"(U|D|L|R)(\d+)", st).groups()
        for i in range(1, abs(int(cn)) + 1):
            if dr == "U":
                y += 1
            elif dr == "D":
                y -= 1
            elif dr == "L":
                x -= 1
            elif dr == "R":
                x += 1
            step_count += 1
            out_tu = ((x, y), step_count, abs(x) + abs(y))
            out.append(out_tu)

    return out


def trace_intersect_points_only(trace1, trace2):
    path1 = list(map(lambda tu: tu[0], trace1))
    path2 = list(map(lambda tu: tu[0], trace2))

    intersect_points = list(set(path1) & set(path2))

    trace1_int = list(filter(lambda tu: tu[0] in intersect_points, trace1))
    trace2_int = list(filter(lambda tu: tu[0] in intersect_points, trace2))

    out = []
    for i in range(len(trace1_int)):
        for j in range(len(trace2_int)):
            if trace1_int[i][0] == trace2_int[j][0]:
                out_tu = (trace1_int[i][0], trace1_int[i][1] + trace2_int[j][1], trace1_int[i][2])
                out.append(out_tu)
    return out


def trace_intersect_info(ss):
    w1 = wire_trace(ss[0])
    w2 = wire_trace(ss[1])
    w_int = trace_intersect_points_only(w1, w2)

    return w_int


trace_res = trace_intersect_info(input_wires)
print('Part 1: ', min(map(lambda tu: tu[2], trace_res)))
print('Part 2: ', min(map(lambda tu: tu[1], trace_res)))
