lines = open('01_input').read().splitlines()

dialPos = 50
zCount = 0
passZcount = 0

for line in lines:
    dr = line[0]
    ln = int(line[1:])

    extras = ln // 100
    passZcount += extras
    ln = ln - 100 * extras

    if ln == 0:
        pass
    elif dr == "L":
        if dialPos !=0 and dialPos - ln <= 0:
            passZcount += 1
        dialPos = (dialPos - ln) % 100
    else:
        if dialPos != 0 and dialPos + ln >= 100:
            passZcount += 1
        dialPos = (dialPos + ln) % 100
    if dialPos == 0:
        zCount += 1

print(zCount)
print(passZcount)