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

    checked_nums = set()

    for i in range(len(disk_state) - 1, 0, -1):
        if (disk_state[i] == " " or disk_state[i] in checked_nums):
            continue

        start = i
        end = i - 1
        current = disk_state[i]
        checked_nums.add(current)
        disk_state[i] = " "

        while (disk_state[end] == current):
            disk_state[end] = " "
            end -= 1
        end += 1
        count = start - end + 1

        inserted = False

        for j in range(end - count + 1):
            if (disk_state[j] != " "):
                continue

            can_be_inserted = True
            for k in range(count):
                if (disk_state[j + k] != " "):
                    can_be_inserted = False
                    break
            
            if (can_be_inserted):
                for k in range(count):
                    disk_state[j + k] = current
                inserted = True
                break

        if (not inserted):
            for j in range(count):
                disk_state[end + j] = current
    
    sum = 0
    for i in range(len(disk_state)):
        if (disk_state[i] == " "):
            continue

        sum += i * disk_state[i]

    print(sum)


if __name__ == "__main__":
    main()