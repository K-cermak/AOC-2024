TOP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

def main():
    with open("day15/15-input.txt", "r") as file:
        data = file.readlines()
        data = [list(line.rstrip()) for line in data]

    with open("day15/15-input2.txt", "r") as file:
        steps = file.readlines()
        steps = [line.rstrip() for line in steps]

    fish_x = 0
    fish_y = 0

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "@":
                fish_x = x
                fish_y = y

    for step in steps:
        for char in step:
            new_x = fish_x
            new_y = fish_y
            direction = None

            if char == "<":
                new_x -= 1
                direction = LEFT
            elif char == ">":
                new_x += 1
                direction = RIGHT
            elif char == "^":
                new_y -= 1
                direction = TOP
            elif char == "v":
                new_y += 1
                direction = DOWN

            if data[new_y][new_x] == "#":
                continue
                
            if data[new_y][new_x] == "." or move(data, new_x, new_y, direction):
                data[new_y][new_x] = "@"
                data[fish_y][fish_x] = "."
                fish_x = new_x
                fish_y = new_y

    sum = 0

    for y, line in enumerate(data):
        for x, char in enumerate(line):            
            if char == "O":
                sum += 100 * y + x 

    print(sum)

def move(data, x, y, direction):
    if (data[y][x] != "O"):
        return False

    x_ = x
    y_ = y

    while data[y_][x_] != "#":
        if data[y_][x_] == ".":
            data[y_][x_] = "O"
            return True
        
        if (direction == TOP):
            y_ -= 1
        elif (direction == DOWN):
            y_ += 1
        elif (direction == LEFT):
            x_ -= 1
        elif (direction == RIGHT):
            x_ += 1

    return False


if __name__ == "__main__":
    main()