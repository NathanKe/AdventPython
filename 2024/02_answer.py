reports = open('02_input').read().split('\n')

safeCount = 0
safeCountX = 0


def report_is_safe(i_levels):
    level_diffs = [i_levels[x]-i_levels[x+1] for x in range(len(i_levels) - 1)]

    safe_decrease = all([ld in [-1, -2, -3] for ld in level_diffs])
    safe_increase = all([ld in [1, 2, 3] for ld in level_diffs])

    if safe_increase or safe_decrease:
        return True
    else:
        return False


for report in reports:
    levels = list(map(int, report.split(" ")))
    if report_is_safe(levels):
        safeCount += 1
        safeCountX += 1
    else:
        print("unsafe: ", levels)
        for ix in range(len(levels)):
            subLevels = levels[:ix]+levels[(ix+1):]
            if report_is_safe(subLevels):
                safeCountX += 1
                break


print(safeCount)
print(safeCountX)
