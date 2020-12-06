import math

with open('AVO\Day3\day3_input.txt') as f:
    raw = f.read()

TEST = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

# Test should give 7 trees

slopes = [(1,1),
            (1,3),
            (1,5),
            (1,7),
            (2,1)]

num_trees_arr = []
res = 1
for slope in slopes:

    input = raw
    lines = input.split("\n")
    height = len(lines)
    width = len(lines[0])
    down = slope[0]
    right = slope[1]
    print("DOWN RIGHT")
    print(down)
    print(right)
    num_trees = 0

    trees = {(x, y)
                    for y, row in enumerate(lines)
                    for x, c in enumerate(row.strip())
                    if c == '#'}
    x = 0
    for y in range(0, height, down):
            if (x, y) in trees:
                num_trees += 1
            x = (x + right) % width 

    print(num_trees)
    num_trees_arr.append(num_trees)
    res = res*num_trees

print(res)



