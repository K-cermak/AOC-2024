def main():
    with open("day09/09-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    disk_state = []
    is_free_space = False
    id = 0

    for char in data[0]:
        if not is_free_space:
            for _ in range(int(char)):
                disk_state.append(id)
            id += 1
        else:
            for _ in range(int(char)):
                disk_state.append(" ")
        
        is_free_space = not is_free_space

    for i in range(len(disk_state) - 1, 0, -1):
        if (disk_state[i] == " "):
            continue

        current = disk_state[i]
        disk_state[i] = " "

        for j in range(i + 1):
            if (disk_state[j] == " "):
                disk_state[j] = current
                break

    sum = 0
    for i in range(len(disk_state)):
        if (disk_state[i] == " "):
            continue

        sum += i * disk_state[i]

    print(sum)


if __name__ == "__main__":
    main()