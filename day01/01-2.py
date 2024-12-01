def main() -> None:
    with open("01-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    list_one = []
    list_two = []

    for line in data:
        line = line.split("   ")
        list_one.append(line[0])
        list_two.append(line[1])

    count = 0
    for i in range(len(list_one)):
        subcount = 0
        for j in range(len(list_two)):
            if list_one[i] == list_two[j]:
                subcount += 1
        
        count += int(list_one[i]) * subcount
    
    print(count)


if __name__ == "__main__":
    main()