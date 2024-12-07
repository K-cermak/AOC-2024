from itertools import product

def main():
    with open("day07/07-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    correct = 0
    for line in data:
        parts = line.split(": ")
        want_result = int(parts[0])

        segments = parts[1].split(" ")
        numbers = []
        for item in segments:
            numbers.append(int(item))

        if(correct_res(numbers, want_result)):
            correct += want_result
    
    print(correct)

def correct_res(numbers, want_result):
    elements = ['+', '*', '|']
    combinations = [''.join(comb) for comb in product(elements, repeat=(len(numbers) - 1))]

    for combination in combinations:
        count = numbers[0]

        for index, number in enumerate(numbers):
            if index == 0:
                continue

            if combination[index - 1] == "+":
                count += number
            elif combination[index - 1] == "*":
                count *= number
            elif combination[index - 1] == "|":
                count = int(str(count) + "" + str(number))
            
        if count == want_result:
            return True


    return False

if __name__ == "__main__":
    main()