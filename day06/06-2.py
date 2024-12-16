TOP = (0, -1)
RIGHT = (1, 0)
BOTTOM = (0, 1)
LEFT = (-1, 0)

def main():
    with open("day06/06-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    count = 0
    player_start = get_player_pos(data)

    for y_iter, line in enumerate(data):
        for x_iter, _ in enumerate(line):
            if data[y_iter][x_iter] == "#" or (x_iter, y_iter) == player_start:
                continue
            
            heading = TOP
            pos = player_start
            found_endless_loop = False

            loops = set()
            x, y = pos
            loops.add((x, y, heading))

            while not (reached_end(data, pos, heading)) and not found_endless_loop:
                x, y = pos
                dx, dy = heading
                new_x = x + dx
                new_y = y + dy

                if data[new_y][new_x] == "#" or (new_x, new_y) == (x_iter, y_iter):
                    heading = turn_right(heading)
                    continue

                pos = (new_x, new_y)
                loop_pos = (new_x, new_y, heading)
                if (loop_pos) not in loops:
                    loops.add(loop_pos)
                else:
                    count += 1
                    found_endless_loop = True

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