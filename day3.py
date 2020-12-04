input = open("inputs/day3.txt", "r")
lines = [line for line in input]

#part 1 
#credit to bbnumber69 on r/adventofcode , my previous solution was mangling the input text
#and I was manually tracking the overflow from 30, it was a mess. His example solution
#makes a lot more sense and helped a lot.
x, y, trees = 0, 0, 0
max_x = len(lines[0])-1
max_y = len(lines)-1

while y < max_y:
    x += 3
    x %= max_x
    y += 1
    if lines[y][x] == "#":
        trees += 1

print(trees)

#part 2

#Decided to make a class but left part 1 up there for posterity. Caused a lot of headache
#since I accidentally referenced the original y and x on line 40 instead of the class 
#specific ones. Big dumb dumb here lol

class Slope:
    def __init__(self, xStep, yStep):
        self.xStep = xStep
        self.yStep = yStep
        self.x = 0
        self.y = 0
        self.trees = 0
    
    def countTrees(self):
        self.trees = 0
        while self.y < max_y:
            self.x += self.xStep
            self.x %= max_x
            self.y += self.yStep
            if lines[self.y][self.x] == "#":
                self.trees += 1
        return self.trees


slope1 = Slope(1,1)
slope2 = Slope(3,1)
slope3 = Slope(5,1)
slope4 = Slope(7,1)
slope5 = Slope(1,2)

print(slope1.countTrees() * slope2.countTrees() 
* slope3.countTrees() * slope4.countTrees() * slope5.countTrees())
