from collections import Counter

data = open('04_input').read().splitlines()
data.append('')


class BingoBoard:
    def __init__(self, in_board):
        self.board = {}
        self.last_called = 0
        row = 0
        for line in in_board:
            col = 0
            for num in line.split():
                self.board[int(num)] = [row, col, "UNMARKED"]
                col += 1
            row += 1

    def play_draw(self, in_num):
        self.last_called = in_num
        if in_num in self.board:
            self.board[in_num][2] = "MARKED"

    def score_or_zero(self):
        marked_set = []
        unmarked_nums = []
        for k, v in self.board.items():
            if v[2] == "MARKED":
                marked_set.append(v)
            elif v[2] == "UNMARKED":
                unmarked_nums.append(k)
        if marked_set:
            most_in_one_row = Counter(map(lambda item: item[0], marked_set)).most_common(1)[0][1]
            most_in_one_col = Counter(map(lambda item: item[1], marked_set)).most_common(1)[0][1]
            if most_in_one_row == 5 or most_in_one_col == 5:
                unmarked_score = sum(unmarked_nums)
                return unmarked_score * self.last_called
        else:
            return 0

    # def board_score(self):
    #    for v in self.board.items():


class BoardSet:
    def __init__(self, in_data_stream):
        self.boards = []
        self.winning_scores = []
        cur_line_set = []
        for line in in_data_stream:
            if line != '':
                cur_line_set.append(line)
            else:
                cur_board = BingoBoard(cur_line_set.copy())
                self.boards.append(cur_board)
                cur_line_set = []

    def play_draw_across_all_boards(self, in_num):
        for board in self.boards:
            board.play_draw(in_num)

    def process_winners(self):
        for index, board in enumerate(self.boards):
            cur_board_score = board.score_or_zero()
            if cur_board_score:
                del self.boards[index]
                self.winning_scores.append(cur_board_score)


my_boards = BoardSet(data[2:])

numbers_to_call = list(map(int, data[0].split(",")))

for num in numbers_to_call:
    my_boards.play_draw_across_all_boards(num)
    my_boards.process_winners()

print("Part 1: ", my_boards.winning_scores[0])
print("Part 2: ", my_boards.winning_scores[-1])
