import itertools
import math


class Moon:
    def __init__(self, i_x, i_y, i_z):
        self.xp = i_x
        self.yp = i_y
        self.zp = i_z
        self.xv = 0
        self.yv = 0
        self.zv = 0


class MoonSet:
    def x_state(self):
        return (self.moon_set[0].xp, self.moon_set[0].xv, 
                self.moon_set[1].xp, self.moon_set[1].xv,
                self.moon_set[2].xp, self.moon_set[2].xv,
                self.moon_set[3].xp, self.moon_set[3].xv)
    
    def y_state(self):
        return (self.moon_set[0].yp, self.moon_set[0].yv, 
                self.moon_set[1].yp, self.moon_set[1].yv,
                self.moon_set[2].yp, self.moon_set[2].yv,
                self.moon_set[3].yp, self.moon_set[3].yv)

    def z_state(self):
        return (self.moon_set[0].zp, self.moon_set[0].zv,
                self.moon_set[1].zp, self.moon_set[1].zv,
                self.moon_set[2].zp, self.moon_set[2].zv,
                self.moon_set[3].zp, self.moon_set[3].zv)

    def __init__(self, m_1, m_2, m_3, m_4):
        self.moon_set = [m_1, m_2, m_3, m_4]
        self.x_cycle_found = False
        self.y_cycle_found = False
        self.z_cycle_found = False
        self.x_cycle = [self.x_state()]
        self.y_cycle = [self.y_state()]
        self.z_cycle = [self.z_state()]
        self.steps = 0

    def gravity(self):
        for pair in itertools.combinations(self.moon_set, 2):
            if pair[0].xp < pair[1].xp:
                pair[0].xv += 1
                pair[1].xv -= 1
            elif pair[0].xp > pair[1].xp:
                pair[0].xv -= 1
                pair[1].xv += 1
            if pair[0].yp < pair[1].yp:
                pair[0].yv += 1
                pair[1].yv -= 1
            elif pair[0].yp > pair[1].yp:
                pair[0].yv -= 1
                pair[1].yv += 1
            if pair[0].zp < pair[1].zp:
                pair[0].zv += 1
                pair[1].zv -= 1
            elif pair[0].zp > pair[1].zp:
                pair[0].zv -= 1
                pair[1].zv += 1

    def velocity(self):
        for moon in self.moon_set:
            moon.xp += moon.xv
            moon.yp += moon.yv
            moon.zp += moon.zv

    def take_step(self):
        self.gravity()
        self.velocity()
        self.steps += 1
        if not self.x_cycle_found:
            cur_x_state = self.x_state()
            if cur_x_state != self.x_cycle[0]:
                self.x_cycle.append(cur_x_state)
            else:
                self.x_cycle_found = True
        if not self.y_cycle_found:
            cur_y_state = self.y_state()
            if cur_y_state != self.y_cycle[0]:
                self.y_cycle.append(cur_y_state)
            else:
                self.y_cycle_found = True
        if not self.z_cycle_found:
            cur_z_state = self.z_state()
            if cur_z_state != self.z_cycle[0]:
                self.z_cycle.append(cur_z_state)
            else:
                self.z_cycle_found = True

    def step_until_cycles(self):
        while not (self.x_cycle_found and self.y_cycle_found and self.z_cycle_found):
            self.take_step()
        return self.x_cycle, self.y_cycle, self.z_cycle

    def state_at_step(self, step_n):
        self.step_until_cycles()
        return self.x_cycle[step_n % len(self.x_cycle)], \
               self.y_cycle[step_n % len(self.y_cycle)], \
               self.z_cycle[step_n % len(self.z_cycle)]

    def energy_at_step(self, step_n):
        xs, ys, zs = self.state_at_step(step_n)
        m1_pot = abs(xs[0]) + abs(ys[0]) + abs(zs[0])
        m2_pot = abs(xs[2]) + abs(ys[2]) + abs(zs[2])
        m3_pot = abs(xs[4]) + abs(ys[4]) + abs(zs[4])
        m4_pot = abs(xs[6]) + abs(ys[6]) + abs(zs[6])

        m1_kin = abs(xs[1]) + abs(ys[1]) + abs(zs[1])
        m2_kin = abs(xs[3]) + abs(ys[3]) + abs(zs[3])
        m3_kin = abs(xs[5]) + abs(ys[5]) + abs(zs[5])
        m4_kin = abs(xs[7]) + abs(ys[7]) + abs(zs[7])

        m1_eng = m1_pot * m1_kin
        m2_eng = m2_pot * m2_kin
        m3_eng = m3_pot * m3_kin
        m4_eng = m4_pot * m4_kin

        return m1_eng + m2_eng + m3_eng + m4_eng


io = Moon(5, 4, 4)
europa = Moon(-11, -11, -3)
ganymede = Moon(0, 7, 0)
callisto = Moon(-13, 2, 10)
moon_set = MoonSet(*[io, europa, ganymede, callisto])

print('Part 1: ', moon_set.energy_at_step(1000))

xlen, ylen, zlen = len(moon_set.x_cycle), len(moon_set.y_cycle), len(moon_set.z_cycle)


def lcm2(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm3(a, b, c):
    return lcm2(lcm2(a, b), c)


print('Part 2: ', lcm3(xlen, ylen, zlen))




