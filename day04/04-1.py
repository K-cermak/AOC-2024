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
    for i in range(len(res)):
        count += analyzer(res, 0, i, 1, 0)
        count += analyzer(res, len(res[0]) - 1, i, -1, 0)

    for i in range(len(res[0])):
        count += analyzer(res, i, 0, 0, 1)
        count += analyzer(res, i, len(res) - 1, 0, -1)

    #diagonals
    for i in range(len(res[0])):
        count += analyzer(res, i, 0, 1, 1)
        count += analyzer(res, i, 0, -1, 1)
        count += analyzer(res, i, 0, 1, -1)
        count += analyzer(res, i, 0, -1, -1)
        count += analyzer(res, i, len(res) - 1, 1, 1)
        count += analyzer(res, i, len(res) - 1, -1, 1)
        count += analyzer(res, i, len(res) - 1, 1, -1)
        count += analyzer(res, i, len(res) - 1, -1, -1)

    for i in range(1, len(res) - 1, 1):
        count += analyzer(res, 0, i, 1, 1)
        count += analyzer(res, 0, i, 1, -1)
        count += analyzer(res, 0, i, -1, 1)
        count += analyzer(res, 0, i, -1, -1)
        count += analyzer(res, len(res[0]) - 1, i, 1, 1)
        count += analyzer(res, len(res[0]) - 1, i, 1, -1)
        count += analyzer(res, len(res[0]) - 1, i, -1, 1)
        count += analyzer(res, len(res[0]) - 1, i, -1, -1)

    print(count)

    

def analyzer(data: list[list], x, y, dx, dy):
    count = 0
    hit = 0

    while y < len(data) and x < len(data[0]) and x >= 0 and y >= 0:
        if ((data[y][x] == "M" and hit == 1)
            or
            (data[y][x] == "A" and hit == 2)
            or
            (data[y][x] == "S" and hit == 3)):
                hit += 1
        else:
            hit = 0
            if data[y][x] == "X":
                hit = 1

        if hit == 4:
            count += 1
            hit = 0

        x += dx
        y += dy

    return count


if __name__ == "__main__":
    main()