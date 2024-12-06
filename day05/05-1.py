def main() -> None:
    with open("day05/05-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    updates_rules = []
    updates = []

    for line in data:
        if "|" in line:
            splitted = line.split("|")
            updates_rules.append((splitted[0], splitted[1]))
        else:
            if line == "":
                continue

            splitted = line.split(",")
            sublist = []
            for i in range(len(splitted)):
                sublist.append(splitted[i])
            updates.append(sublist)


    count = 0

    for update in updates:
        before_elements = []
        for rule in update:
            pre_items = set()
            get_before(updates_rules, rule, pre_items)
            before_elements.append(pre_items)
        
        is_correct = True
        for index, rule in enumerate(update):
            for i in range(index):
                if rule in before_elements[i]:
                    is_correct = False
                    break

        if is_correct:
            count += int(update[(len(update) // 2)])

    print(count)


def get_before(updates_rules, current, pre_items):
    for (bef, after) in updates_rules:
        if after == current:
            pre_items.add(bef)


if __name__ == "__main__":
    main()