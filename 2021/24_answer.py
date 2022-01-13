import re

instr_stream = open('24_input').read().splitlines()

w = 0
x = 0
y = 0
z = 0


def parse(stream):
    global w
    global x
    global y
    global z
    for instr in stream:
        i_type, *args = instr.split(" ")
        print(i_type, *args)
        if re.match(r"\d", args[1]):
            b = args[1]
        elif args[1] in ['w', 'x', 'y', 'z']:
            b = str(globals()[args[1]])
        else:
            b = args[1]

        if i_type == "inp":
            globals()[args[0]] = args[1]
        elif i_type == "add":
            globals()[args[0]] = eval("(" + str(globals()[args[0]]) + ") + " + b)
        elif i_type == "mul":
            globals()[args[0]] = eval("(" + str(globals()[args[0]]) + ") * " + b)
        elif i_type == "div":
            globals()[args[0]] = eval("(" + str(globals()[args[0]]) + ") // " + b)
        elif i_type == "mod":
            globals()[args[0]] = eval("(" + str(globals()[args[0]]) + ") % " + b)
        elif i_type == "add":
            globals()[args[0]] = eval("int((" + str(globals()[args[0]]) + ") == " + b + ")")


parse(instr_stream)
print(w, x, y, z)
