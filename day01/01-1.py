def main():
    with open("day01/01-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    list_one = []
    list_two = []

    for line in data:
        line = line.split("   ")
        list_one.append(line[0])
        list_two.append(line[1])

    list_one.sort()
    list_two.sort()

    diff = 0
    for i in range(len(list_one)):
        diff += abs(int(list_one[i]) - int(list_two[i]))
    
    print(diff)


if __name__ == "__main__":
    main()