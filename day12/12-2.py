TOP = 1
RIGHT = 2
BOTTOM = 3
LEFT = 4

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
    pos_neigbours = {}

    for pos in positions:
        already_counted[pos] = True
        x_, y_ = pos
        if neighbour_status(data, x_ + 1, y_, data[y][x]) == 1:
            pos_neigbours[(x_ , y_, LEFT)] = False
        if neighbour_status(data, x_ - 1, y_, data[y][x]) == 1:
            pos_neigbours[(x_ , y_, RIGHT)] = False
        if neighbour_status(data, x_, y_ + 1, data[y][x]) == 1:
            pos_neigbours[(x_ , y_, TOP)] = False
        if  neighbour_status(data, x_, y_ - 1, data[y][x]) == 1:
            pos_neigbours[(x_ , y_, BOTTOM)] = False

    diffs = 0

    for pos, used in pos_neigbours.items():
        if used:
            continue

        x, y, heading = pos
        possibles = []
        possibles.append(pos)
        pos_neigbours[pos] = True
        diffs += 1

        made_change = True

        while made_change:
            made_change = False

            for pos_, used_ in pos_neigbours.items():
                xa, ya, heading_ = pos_

                if used_ or (heading_ != heading):
                    continue

                for x_, y_, _ in possibles:
                    if (x_ == xa and abs(ya - y_) == 1) or \
                        (y_ == ya and abs(xa - x_) == 1):
                        possibles.append(pos_)
                        pos_neigbours[pos_] = True
                        made_change = True

    return diffs * len(positions)


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