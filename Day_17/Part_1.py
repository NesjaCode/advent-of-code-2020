import copy

def parse_input():
    lines = open("input.txt").read().split("\n")
    tempArr = []
    for cell in lines:
        tempArr.append(list(cell))
    return tempArr

def check_neighbors(x, y, z, maxLength, space):
    counter = 0
    for i in range(max(z - 1, 0), min(z + 2, maxLength)):
        for j in range(max(y - 1, 0), min(y + 2, maxLength)):
            for a in range(max(x - 1, 0), min(x+ 2, maxLength)):
                if((i != z or j != y or a != x) and space[i][j][a] == '#'):
                    counter += 1
    return counter

init_size = 23
z_offset = int((init_size-1)/2)
space = [[['.' for i in range(init_size)] for i in range(init_size)] for i in range(init_size)]
for y, i in enumerate(parse_input()):
    for x, j in enumerate(i):
        space[z_offset][y + z_offset - 1][x + z_offset - 1] = j

counter = 0
while counter < 6:
    tempSpace = [[['.' for i in range(init_size)] for i in range(init_size)] for i in range(init_size)]
    for z, i in enumerate(space):
        for y, j in enumerate(i):
            for x, a in enumerate(j):
                neighbors = check_neighbors(x, y, z, init_size - 1, space)
                if(a == "#" and (neighbors == 2 or neighbors == 3)):
                    tempSpace[z][y][x] = "#"
                elif(a == "." and neighbors == 3):
                    tempSpace[z][y][x] = "#"
    space = copy.deepcopy(tempSpace)
    counter += 1

"""
-> Function to read the 3D-space (like in example)
for i, z in enumerate(space):
    print("z = ", i-z_offset)
    for y in z:
        print(y)
    print()
"""

result = 0
for z in space:
    for y in z:
        for x in y:
            if(x == "#"):
                result += 1
print(result)