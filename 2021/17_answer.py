targ_text = open('17_input').read().splitlines()[0]

x_text, y_text = targ_text.split(': ')[1].split(', ')

x_low, x_high = [int(x) for x in x_text.split('=')[1].split('..')]
y_low, y_high = [int(y) for y in y_text.split('=')[1].split('..')]


targ_area = set()
for x in range(x_low, x_high + 1):
    for y in range(y_low, y_high + 1):
        targ_area.add((x, y))


class Probe:
    def __init__(self, i_x_vel, i_y_vel):
        self.x_vel = i_x_vel
        self.y_vel = i_y_vel
        self.x_pos = 0
        self.y_pos = 0
        self.path = {(self.x_pos, self.y_pos)}
        self.max_y = 0

    def step(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        if self.x_vel > 0:
            self.x_vel -= 1
        elif self.x_vel < 0:
            self.x_vel += 1
        self.y_vel -= 1
        self.path.add((self.x_pos, self.y_pos))
        if self.y_pos > self.max_y:
            self.max_y = self.y_pos

    def fire(self):
        while self.y_pos > y_low:
            self.step()


success_max_y = 0
success_count = 0
for x in range(0, x_high + 1):
    for y in range(y_low, 500):
        c_p = Probe(x, y)
        c_p.fire()
        if c_p.path.intersection(targ_area):
            if c_p.max_y > success_max_y:
                success_max_y = c_p.max_y
            success_count += 1


print("Part 1: ", success_max_y)
print("Part 2: ", success_count)
