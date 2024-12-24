def main():
    with open("day14/14-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    sectors = [0, 0, 0, 0]

    for line in data:
        line = line.split(" ")

        p = line[0].split("=")
        p = p[1].split(",")
        v = line[1].split("=")
        v = v[1].split(",")

        px = int(p[0])
        py = int(p[1])
        vx = int(v[0])
        vy = int(v[1])

        px = (px + (vx * 100)) % 101
        py = (py + (vy * 100)) % 103

        if px == 50 or py == 51:
            continue

        if px < 50 and py < 51:
            sectors[0] += 1
        elif px > 50 and py < 51:
            sectors[1] += 1
        elif px < 50 and py > 51:
            sectors[2] += 1
        elif px > 50 and py > 51:
            sectors[3] += 1

    print(sectors)
    sum = sectors[0]
    for i in range(1, 4):
        sum *= sectors[i]
    
    print(sum)


if __name__ == "__main__":
    main()