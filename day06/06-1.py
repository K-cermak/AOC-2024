TOP = (0, -1)
RIGHT = (1, 0)
BOTTOM = (0, 1)
LEFT = (-1, 0)

def main():
    with open("day06/06-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    count = 1
    heading = TOP
    pos = get_player_pos(data)
    visited = set()
    visited.add(pos)

    while not (reached_end(data, pos, heading)):
        x, y = pos
        dx, dy = heading
        new_x = x + dx
        new_y = y + dy

        if data[new_y][new_x] == "#":
            heading = turn_right(heading)
            continue

        pos = (new_x, new_y)
        if pos not in visited:
            count += 1
            visited.add(pos)

    print(count)


def get_player_pos(data):
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "^":
                return (x, y)
            
def reached_end(data, pos, heading):
    x, y = pos
    if y == 0 and heading == TOP:
        return True
    if y == len(data) - 1 and heading == BOTTOM:
        return True
    if x == 0 and heading == LEFT:
        return True
    if x == len(data[0]) - 1 and heading == RIGHT:
        return True

    return False


def turn_right(heading):
    if heading == TOP:
        return RIGHT
    if heading == RIGHT:
        return BOTTOM
    if heading == BOTTOM:
        return LEFT
    if heading == LEFT:
        return TOP

if __name__ == "__main__":
    main()