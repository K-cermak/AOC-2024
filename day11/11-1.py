GENS = 25

def main():
    with open("day11/11-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    line = data[0].split(" ")
    stones = []
    for stone in line:
        stones.append(stone)

    new_stones = []
    for _ in range(GENS):
        for stone in stones:
            if stone == "0":
                new_stones.append("1")
            elif len(stone) % 2 == 0:
                new_stones.append(str(int(stone[0:len(stone)//2])))
                new_stones.append(str(int(stone[len(stone)//2:])))
            else:
                new_stones.append(str(int(stone) * 2024))

        stones = new_stones
        new_stones = []

    print(len(stones))
    


if __name__ == "__main__":
    main()