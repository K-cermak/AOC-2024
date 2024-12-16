def main():
    with open("day10/10-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    res = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (char == "0"):
                find_dest(data, x, y, x, y, res)
    
    count = 0
    for _, value in res.items():
        count += value
    
    print(count)


def find_dest(data, x, y, x_init, y_init, res):
    current_val = int(data[y][x])
    if (current_val == 9):
        res[(x_init, y_init)] = res.get((x_init, y_init), 0) + 1
        return

    if (x > 0 and data[y][x - 1] != "." and int(data[y][x - 1]) == current_val + 1):
        find_dest(data, x - 1, y, x_init, y_init, res)
    if (x < len(data[y]) - 1 and data[y][x + 1] != "." and int(data[y][x + 1]) == current_val + 1):
        find_dest(data, x + 1, y, x_init, y_init, res)
    if (y > 0 and data[y - 1][x] != "." and int(data[y - 1][x]) == current_val + 1):
        find_dest(data, x, y - 1, x_init, y_init, res)
    if (y < len(data) - 1 and data[y + 1][x] != "." and int(data[y + 1][x]) == current_val + 1):
        find_dest(data, x, y + 1, x_init, y_init, res)
        



if __name__ == "__main__":
    main()