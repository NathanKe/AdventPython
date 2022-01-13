from enum import Enum


class AmphiType(Enum):
    A = 1
    B = 2
    C = 3
    D = 4


class Locations(Enum):
    A_1 = 1
    A_2 = 2
    B_1 = 3
    B_2 = 4
    C_1 = 5
    C_2 = 6
    D_1 = 7
    D_2 = 8
    L_O = 9
    L_I = 10
    R_O = 11
    R_I = 12
    H_AB = 13
    H_BC = 14
    H_CD = 15


class Amphipod:
    def __init__(self, in_loc, in_type):
        self.loc = in_loc
        self.a_type = in_type
        self.hall_lock = False
        if self.a_type.name[0] == self.loc.name[0]:
            self.correct = True
        else:
            self.correct = False
        self.energy_usage = 0

    def possible_moves(self):
        if self.hall_lock:
            if self.a_type.name[0] == 'A':
                return [Locations.A_1, Locations.A_2]
            elif self.a_type.name[0] == 'B':
                return [Locations.B_1, Locations.B_2]
            elif self.a_type.name[0] == 'C':
                return [Locations.C_1, Locations.C_2]
            elif self.a_type.name[0] == 'D':
                return [Locations.D_1, Locations.D_2]
        else:
            halls = [Locations.H_AB, Locations.H_BC, Locations.H_CD, Locations.L_I, Locations.L_O, Locations.R_I,
                     Locations.R_O]
            if self.a_type.name[0] == 'A':
                return [Locations.A_1, Locations.A_2] + halls
            elif self.a_type.name[0] == 'B':
                return [Locations.B_1, Locations.B_2] + halls
            elif self.a_type.name[0] == 'C':
                return [Locations.C_1, Locations.C_2] + halls
            elif self.a_type.name[0] == 'D':
                return [Locations.D_1, Locations.D_2] + halls
