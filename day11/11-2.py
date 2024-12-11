## Inspired from: https://github.com/MeisterLLD/aoc2024/blob/main/11.py

GENS = 75

def main():
    with open("day11/11-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    line = data[0].split(" ")
    count = 0
    for stone in line:
        count += calc(GENS, int(stone))

    print(count)


dict = {}

def calc(steps, stone):
    if (steps, stone) in dict:
        return dict[(steps, stone)]

    if (steps == 0):
        return 1
    
    if (stone == 0):
        return calc(steps - 1, 1)
    
    len_ = len(str(stone))

    if (len_ % 2 != 0):
        res = calc(steps - 1, stone * 2024)
        dict[(steps, stone)] = res
        return res
    
    num1 = int(str(stone)[0:len_//2])
    num2 = int(str(stone)[len_//2:])
    return calc(steps - 1, num1) + calc(steps - 1, num2)
    


if __name__ == "__main__":
    main()