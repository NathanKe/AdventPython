import itertools

target = 36000000


def presents_by_elf(elf):
    x = [0 for i in range(elf - 1)]
    x.append(10 * elf)
    return x * 50


masks = [presents_by_elf(i) for i in range(1000)]

zipped = itertools.zip_longest(*masks, fillvalue=0)

summed = map(sum, zipped)

# first_greater_than_target = list(filter(lambda i: i >= target, summed))[0]
