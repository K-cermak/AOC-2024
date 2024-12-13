def main():
    with open("day12/12-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    price = 0
    already_counted = {}

    for y in range(len(data)):
        for x in range(len(data[0])):
            price += analyze(data, x, y, already_counted)

    print(price)


def analyze(data, x, y, already_counted):
    if (x, y) in already_counted:
        return 0

    positions = set()

    rec_neighbours(data, x, y, positions, data[y][x])
    diff_neighbour = 0;

    for pos in positions:
        already_counted[pos] = True
        x_, y_ = pos
        diff_neighbour += neighbour_status(data, x_ + 1, y_, data[y][x])
        diff_neighbour += neighbour_status(data, x_ - 1, y_, data[y][x])
        diff_neighbour += neighbour_status(data, x_, y_ + 1, data[y][x])
        diff_neighbour += neighbour_status(data, x_, y_ - 1, data[y][x])

    return diff_neighbour * len(positions)



def rec_neighbours(data, x, y, positions, char):
    if (x, y) in positions:
        return

    if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data):
        return
    
    if data[y][x] != char:
        return

    positions.add((x, y))
    rec_neighbours(data, x + 1, y, positions, char)
    rec_neighbours(data, x - 1, y, positions, char)
    rec_neighbours(data, x, y + 1, positions, char)
    rec_neighbours(data, x, y - 1, positions, char)

def neighbour_status(data, x, y, char):
    if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data):
        return 1

    if data[y][x] != char:
        return 1

    return 0



if __name__ == "__main__":
    main()