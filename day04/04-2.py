def main() -> None:
    with open("day04/04-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    res = []
    for line in data:
        subres = []
        for char in line:
            subres.append(char)
        res.append(subres)

    count = 0
    for y in range(1, len(res) - 1):
        for x in range(1, len(res[0]) - 1):
            count += analyzer(res, x, y)

    print(count)

    

def analyzer(data: list[list], x, y):
    if data[y][x] != "A":
        return 0

    if ((data[y + 1][x - 1] == "M" and data[y - 1][x + 1] == "S")
        and
        (data[y + 1][x + 1] == "S" and data[y - 1][x - 1] == "M")):
            return 1


    if ((data[y + 1][x - 1] == "S" and data[y - 1][x + 1] == "M")
        and
        (data[y + 1][x + 1] == "S" and data[y - 1][x - 1] == "M")):
            return 1
    
    if ((data[y + 1][x - 1] == "M" and data[y - 1][x + 1] == "S")
        and
        (data[y + 1][x + 1] == "M" and data[y - 1][x - 1] == "S")):
            return 1

    if ((data[y + 1][x - 1] == "S" and data[y - 1][x + 1] == "M")
        and
        (data[y + 1][x + 1] == "M" and data[y - 1][x - 1] == "S")):
            return 1

    return 0


if __name__ == "__main__":
    main()