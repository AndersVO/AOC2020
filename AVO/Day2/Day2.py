with open("H:\Code\AOC2020\AOC2020\AVO\Day2\Day2_input.txt") as f:
    inputs = [line.strip() for line in f]
    #print(inputs)

TEST = ["1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"]
count = 0
count2 = 0
for line in inputs:
    counts, char, password =  line.strip().split()
    low, high = [int(n) for n in counts.split('-')]
    char = char[0]

    num_chars = password.count(char)

    if num_chars >= low and num_chars <= high:
        count += 1

    pos1 = password[low-1] is char
    pos2 = password[high-1] is char

    if (pos1 and not pos2) or (not pos1 and pos2):
        count2 +=1
    
print(count)
print(count2)

















