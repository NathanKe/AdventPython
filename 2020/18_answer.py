import re

lines = open('18_input').read().splitlines()


def process(line):
    if "(" in line:
        simple_evals = re.findall(r"\([^\(|^\)]+\)", line)
        for se in simple_evals:
            res = process(se[1:-1])
            line = line.replace(se, res)
        return process(line)
    elif "+" in line or "*" in line:
        terms = line.split(" ")
        first_expr = terms[0:3]
        expr_tail = terms[3:]
        first_expr_eval = str(eval(''.join(first_expr)))

        line = (first_expr_eval + ' ' + ' '.join(expr_tail)).strip()
        return process(line)
    else:
        return line


def process2(line):
    if "(" in line:
        simple_evals = re.findall(r"\([^\(|^\)]+\)", line)
        for se in simple_evals:
            res = process2(se[1:-1].strip())
            line = line.replace(se, res)
        return process2(line)
    elif "+" in line:
        terms = line.split()
        first_plus = terms.index('+')
        first_plus_expr = terms[first_plus - 1: first_plus + 2]
        expr_head = terms[:first_plus - 1]
        expr_tail = terms[first_plus + 2:]

        first_plus_expr_eval = str(eval(''.join(first_plus_expr)))
        line = ' '.join(expr_head).strip() + ' ' + first_plus_expr_eval + ' ' + ' '.join(expr_tail).strip()
        return process2(line.strip())
    elif "*" in line:
        terms = line.split(" ")
        first_expr = terms[0:3]
        expr_tail = terms[3:]
        first_expr_eval = str(eval(''.join(first_expr)))

        line = (first_expr_eval + ' ' + ' '.join(expr_tail)).strip()
        return process2(line)
    else:
        return line.strip()


print('Part 1: ', sum(map(lambda x: int(process(x)), lines)))
print('Part 1: ', sum(map(lambda x: int(process2(x)), lines)))
