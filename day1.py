input = open("inputs/day1.txt", "r")
lines = input.readlines()
#part 1
# for i in range(len(lines)):
#     for j in range(i+1, len(lines)):
#         if (int(lines[i])+int(lines[j]) == 2020):
#             print(int(lines[i])*int(lines[j]))
#part 2
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        for k in range(i+2, len(lines)):
            if (int(lines[i])+int(lines[j])+int(lines[k]) == 2020):
                print(int(lines[i])*int(lines[j])*int(lines[k]))