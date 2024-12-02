def main() -> None:
    with open("day02/02-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    count = 0

    for line in data:
        line = line.split(" ")
        increasing = False
        correct = True

        if int(line[0]) < int(line[1]):
            increasing = True

        for i in range(len(line) - 1):
            num1 = int(line[i])
            num2 = int(line[i + 1])
            diff = abs(num1 - num2)

            if diff < 1 or diff > 3:
                correct = False
                break

            if increasing and num2 < num1:
                correct = False
                break
            elif not increasing and num2 > num1:
                correct = False
                break

        if correct:
            count += 1

    print(count)



if __name__ == "__main__":
    main()