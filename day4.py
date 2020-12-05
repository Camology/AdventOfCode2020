import re

input = open("inputs/day4.txt", "r")
#credit to themanush on r/adventofcode I was very confused how to nicely read this in
lines = [line.replace("\n", " ") for line in input.read().split("\n\n")]

#part1
requiredItems = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
acceptedPP = 0
for line in lines:
    if all(item in line for item in requiredItems):
        acceptedPP+=1
print(acceptedPP)

#part2

acceptedPP2 = 0
for line in lines:
    if all(item in line for item in requiredItems):
        print("Original:", line)
        fields = []
        birthYear = re.search("byr:\\d{4}",line)
        if (int(birthYear.group()[4:]) >= 1920 and int(birthYear.group()[4:]) <= 2002):
            fields.insert(0,birthYear.group())
            print("birth year is good")
        issueYear = re.search("iyr:\\d{4}",line)
        if (int(issueYear.group()[4:]) >= 2010 and int(issueYear.group()[4:]) <= 2020):
            fields.insert(0,issueYear.group())
            print("issue year is good")
        expYear = re.search("eyr:\\d{4}",line)
        if (int(expYear.group()[4:]) >= 2020 and int(expYear.group()[4:]) <= 2030):
            fields.insert(0,expYear.group())
            print("exp year is good")
        height = re.search("hgt:\\d{2,3}[a-z]{2}",line)
        if height:
            value = re.search("\\d{2,3}", height.group())
            if value:
                if height.group().find("cm") != -1:
                    if int(value.group()) >= 150 and int(value.group()) <= 193:
                        print("height is good")
                        fields.insert(0,height.group())
                else:
                    if int(value.group()) >= 59 and int(value.group()) <= 76:
                        print("height is good")
                        fields.insert(0,height.group())
        hairColor = re.search("hcl:#[a-f0-9]{6}", line)
        if hairColor:
            print("hair color is good")
            fields.insert(0,hairColor.group())
        eyeColor = re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth)",line)
        if eyeColor:
            print("eye color is good")
            fields.insert(0,eyeColor.group())
        passportID = re.search("pid:\\d{9}",line)
        if passportID:
            print("ID is good")
            fields.insert(0,passportID.group())
        
        if len(fields) == 7:
            print("Accepted:", line)
            acceptedPP2+=1
        print("------")
print(acceptedPP2)

