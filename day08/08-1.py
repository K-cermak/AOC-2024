def main():
    with open("day08/08-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]


    signal_pos = set()
    x_max = len(data[0])
    y_max = len(data)

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == ".":
                continue

            for y_, line_ in enumerate(data):
                for x_, char_ in enumerate(line_): 
                    if (char_ != char) or (x_ == x and y_ == y):
                        continue
                    
                    x_move = x_ - x
                    y_move = y_ - y

                    x_move *= 2
                    y_move *= 2

                    x_move += x
                    y_move += y

                    if x_move >= 0 and y_move >= 0 and x_move < x_max and y_move < y_max:
                        signal_pos.add((x_move, y_move))

    print(len(signal_pos))


if __name__ == "__main__":
    main()