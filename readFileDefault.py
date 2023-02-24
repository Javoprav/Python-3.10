filename = "readFileDefault.py" # этот код
f = open(filename)
lines = []
for line in f:
    lines.append(line.strip())
print(lines)