from random import randint


f = open("add_ws.txt", "w")

line_count = 20
q_line = 4

for x in range(line_count):
    for y in range(q_line):
        a = randint(1,9)
        b = randint(1,9)
        f.write("%d + %d = _____" % (a, b))
        if y != q_line - 1:
            f.write(" " * 5)

    if x != line_count - 1:
        f.write("\n\n\n")

f.close()
