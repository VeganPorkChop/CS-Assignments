lines = open("lines.txt", "w")
for i in range(99):
    lines.write("Line %d\n" % (i + 1))