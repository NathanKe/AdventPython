class Rope:
    def __init__(self, in_knot_count):
        self.rope = []
        self.knot_count = in_knot_count
        for k in range(in_knot_count):
            self.rope.append(0 + 0j)
        self.tail_visits = set()

    def catch_up_tail(self, knot_index):
        head = self.rope[knot_index]
        tail = self.rope[knot_index + 1]
        # close enough, do nothing
        if abs(head - tail) <= abs(1+1j):
            pass
        # orthogonal catch up
        elif abs(head - tail) == 2:
            self.rope[knot_index + 1] += (head - tail)/2
        # diagonal catch up
        else:
            if head.real > tail.real and head.imag > tail.imag:
                self.rope[knot_index + 1] += 1 + 1j
            elif head.real > tail.real and head.imag < tail.imag:
                self.rope[knot_index + 1] += 1 - 1j
            elif head.real < tail.real and head.imag > tail.imag:
                self.rope[knot_index + 1] += -1 + 1j
            elif head.real < tail.real and head.imag < tail.imag:
                self.rope[knot_index + 1] += -1 - 1j
            else:
                print("oh god something went wrong")

        # if at second to last knot, last knot catch up has processed
        # add new tail to set
        if knot_index == self.knot_count - 2:
            self.tail_visits.add(self.rope[-1])
        # else tail recur.  Quite literally tail recur
        else:
            self.catch_up_tail(knot_index + 1)

    def move_head_one(self, in_dir):
        self.rope[0] += in_dir
        self.catch_up_tail(0)
        return None

    def execute_instruction(self, in_instr):
        direction_txt, count_txt = in_instr.split(" ")

        if direction_txt == "L":
            direction = -1
        elif direction_txt == "R":
            direction = 1
        elif direction_txt == "U":
            direction = 1j
        elif direction_txt == "D":
            direction = -1j
        else:
            direction = 0
            print("text parsing error")

        for _ in range(int(count_txt)):
            self.move_head_one(direction)

    def simulate(self, instr_set):
        for instr in instr_set:
            self.execute_instruction(instr)
        return len(self.tail_visits)


input_instructions = open('09_input').read().splitlines()

rope1 = Rope(2)
print(rope1.simulate(input_instructions))

rope2 = Rope(10)
print(rope2.simulate(input_instructions))
