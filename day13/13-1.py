def main():
    with open("day13/13-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    count = 0

    ax = 0
    ay = 0
    bx = 0
    by = 0
    fx = 0
    fy = 0

    for line_ in data:
        if (line_ == ""):
            continue

        line = line_.split(" ")
        if line[0] == "Button" and line[1] == "A:":
            ax = int(line[2][2:line[2].index(",")])
            ay = int(line[3][2:])
        elif line[0] == "Button" and line[1] == "B:":
            bx = int(line[2][2:line[2].index(",")])
            by = int(line[3][2:])
        else:
            fx = int(line[1][2:line[1].index(",")])
            fy = int(line[2][2:])

        if (ax != 0) and (bx != 0) and (fx != 0):
            res = process(ax, ay, bx, by, fx, fy)
            if (res is not None):
                count += res
            ax = 0
            ay = 0
            bx = 0
            by = 0
            fx = 0
            fy = 0
    
    print(count)

def process(ax, ay, bx, by, fx, fy):
    best_sum = None

    for a in range(100):
        for b in range(100):
            if (a * ax + b * bx) == fx and (a * ay + b * by) == fy:
                if best_sum is None or ((3 * a) + b < best_sum):
                    best_sum = (3 * a) + b
    
    return best_sum
            


if __name__ == "__main__":
    main()