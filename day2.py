input = open("inputs/day2.txt", "r")
lines = input.read().splitlines()

#part1
passCounter = 0
for line in lines:
    min = line[0:line.find("-")]
    max = line[line.find("-")+1:line.find(" ")]
    character = line[line.find(" ")+1:line.find(":")]
    password = line[line.find(":")+2:]

    letterCounter = 0
    for letter in password:
        if letter == character:
            letterCounter+=1
    if letterCounter > int(max) or letterCounter < int(min):
        continue
    else: 
        passCounter+=1
    

print(passCounter)

#part2
passCounter2 = 0
for line in lines:
    pos1 = line[0:line.find("-")]
    pos2 = line[line.find("-")+1:line.find(" ")]
    character = line[line.find(" ")+1:line.find(":")]
    password = line[line.find(":")+2:]


    if password[int(pos1)-1] == character and password[int(pos2)-1] != character:
        passCounter2+=1
    if password[int(pos1)-1] != character and password[int(pos2)-1] == character:
        passCounter2+=1

print(passCounter2)
