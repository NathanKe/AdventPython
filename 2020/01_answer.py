input_nums = list(map(int, open('01_input').read().splitlines()))

ans1 = 0
ans2 = 0
for num1 in input_nums:
    for num2 in input_nums:
        if num1 + num2 == 2020:
            ans1 = num1 * num2
        for num3 in input_nums:
            if num1 + num2 + num3 == 2020:
                ans2 = num1 * num2 * num3

print(ans1)
print(ans2)
