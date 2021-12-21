class DiracDice:
    def __init__(self, p1_start, p2_start):
        self.p1score = 0
        self.p2score = 0
        self.p1space = p1_start
        self.p2space = p2_start
        self.roll_count = 0
        self.game_over = False
        self.die_val_list = range(1, 101)
        self.die_index = 0

    def roll_and_advance(self):
        r_v = self.die_val_list[self.die_index]
        self.die_index += 1
        self.die_index %= 100
        return r_v

    def roll_each(self, win_score):
        p1_roll_a = self.roll_and_advance()
        p1_roll_b = self.roll_and_advance()
        p1_roll_c = self.roll_and_advance()
        p1_roll = p1_roll_a + p1_roll_b + p1_roll_c

        self.roll_count += 3

        self.p1space = (self.p1space + p1_roll) % 10
        self.p1score += self.p1space + 1

        if self.p1score >= win_score:
            return True

        p2_roll_a = self.roll_and_advance()
        p2_roll_b = self.roll_and_advance()
        p2_roll_c = self.roll_and_advance()
        p2_roll = p2_roll_a + p2_roll_b + p2_roll_c

        self.roll_count += 3

        self.p2space = (self.p2space + p2_roll) % 10
        self.p2score += (self.p2space + 1)

        if self.p2score >= win_score:
            return True

        return False

    def play_to_win(self, win_score):
        while not self.game_over:
            self.game_over = self.roll_each(win_score)

        return self.roll_count * min(self.p1score, self.p2score)


part1_game = DiracDice(0, 2)
print("Part 1: ", part1_game.play_to_win(1000))

state_cache = {}


def count_win(p1, p2, s1, s2, turn):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    if (p1, p2, s1, s2, turn) in state_cache:
        return state_cache[(p1, p2, s1, s2, turn)]

    answer = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                if turn == 'one':
                    new_p1 = (p1 + d1 + d2 + d3) % 10
                    new_s1 = s1 + new_p1 + 1
                    p1_win_subcall, p2_win_subcall = count_win(new_p1, p2, new_s1, s2, "two")
                    answer = (answer[0] + p1_win_subcall, answer[1] + p2_win_subcall)
                else:
                    new_p2 = (p2 + d1 + d2 + d3) % 10
                    new_s2 = s2 + new_p2 + 1
                    p1_win_subcall, p2_win_subcall = count_win(p1, new_p2, s1, new_s2, "one")
                    answer = (answer[0] + p1_win_subcall, answer[1] + p2_win_subcall)
    state_cache[(p1, p2, s1, s2, turn)] = answer
    return answer


print("Part 2: ", max(count_win(0, 2, 0, 0, "one")))
