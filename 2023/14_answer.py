import numpy

rock_text = open('14_input').read().splitlines()

height = len(rock_text)
width = len(rock_text[0])

rock_matrix = numpy.mat(list(map(list, rock_text)))


def shuffle_north(i_mat):
    done_shuffling = False
    while not done_shuffling:
        done_shuffling = True
        for row_n in range(1, height):
            for col_n in range(width):
                if i_mat[row_n, col_n] == 'O':
                    if i_mat[row_n - 1, col_n] == '.':
                        i_mat[row_n - 1, col_n] = 'O'
                        i_mat[row_n, col_n] = '.'
                        done_shuffling = False
    return i_mat


def shuffle_cycle(i_mat):
    i_mat = shuffle_north(i_mat)
    i_mat = numpy.rot90(i_mat, 3)
    i_mat = shuffle_north(i_mat)
    i_mat = numpy.rot90(i_mat, 3)
    i_mat = shuffle_north(i_mat)
    i_mat = numpy.rot90(i_mat, 3)
    i_mat = shuffle_north(i_mat)
    i_mat = numpy.rot90(i_mat, 3)
    return i_mat


def load_calc(i_mat):
    load = 0
    for row_n in range(height):
        for col_n in range(width):
            if i_mat[row_n, col_n] == 'O':
                load += height - row_n
    return load





# print(load_calc(shuffle_north(rock_matrix)))
