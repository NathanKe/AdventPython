import numpy

raw_patterns = open('13_input').read().split('\n\n')


def zero_one_matrix(pattern_text):
    out_mat = []
    for row in pattern_text.splitlines():
        m_row = []
        for column in row:
            if column == "#":
                m_row.append(1)
            else:
                m_row.append(0)
        out_mat.append(m_row)
    return numpy.mat(out_mat)


def mirror_check(i_mat, last_row_included_in_top_half, part):
    top = i_mat[:last_row_included_in_top_half]
    bot = i_mat[last_row_included_in_top_half:]

    height = min(len(top), len(bot))

    redux_top = top[len(top) - height:]
    redux_bot = bot[:height]

    flip_bot = numpy.flipud(redux_bot)
    negate_flip_bot = numpy.multiply(flip_bot, -1)

    overlay = numpy.add(redux_top, negate_flip_bot)

    if part == 1:
        return not numpy.any(overlay)
    if part == 2:
        return numpy.sum(numpy.absolute(overlay)) == 1


def mirror_metric(i_mat, part):
    out_metric = 0
    for mirror_line in range(1, len(i_mat)):
        if mirror_check(i_mat, mirror_line, part):
            out_metric += mirror_line
            break
    return out_metric


def two_way_mirror_metric(i_mat, part):
    columns_left_metric = mirror_metric(numpy.transpose(i_mat), part)
    rows_above_metric = mirror_metric(i_mat, part)
    return columns_left_metric + 100 * rows_above_metric


print(sum(map(lambda pt: two_way_mirror_metric(zero_one_matrix(pt), 1), raw_patterns)))
print(sum(map(lambda pt: two_way_mirror_metric(zero_one_matrix(pt), 2), raw_patterns)))
