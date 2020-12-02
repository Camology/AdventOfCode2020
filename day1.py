import itertools
input = open("inputs/day1.txt", "r")
lines = input.read().splitlines()
#part 1

for x, y in itertools.combinations(lines, 2):
    if (int(x)+int(y) == 2020):
        print(int(x)*int(y))

#part 2
for x, y, z in itertools.combinations(lines, 3):
    if (int(x)+int(y)+int(z) == 2020):
        print(int(x)*int(y)*int(z))