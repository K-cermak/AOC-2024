import re

def main() -> None:
    with open("day03/03-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    count = 0
    regex = "(mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\))"
    allowed = True

    for line in data:
        match = re.findall(regex, line)
        for m in match:
            if m == "do()":
                allowed = True
            elif m == "don't()":
                allowed = False
            elif allowed:
                m = m[4:-1]
                m = m.split(",")
                num1 = int(m[0])
                num2 = int(m[1])

                count += num1 * num2

    print(count)


if __name__ == "__main__":
    main()