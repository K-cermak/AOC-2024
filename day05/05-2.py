from collections import defaultdict, deque

def main():
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

        if not is_correct(update, before_elements):
            topological_sort(update, updates_rules)
            count += int(update[(len(update) // 2)])

    print(count)


def get_before(updates_rules, current, pre_items):
    for (bef, after) in updates_rules:
        if after == current:
            pre_items.add(bef)


def is_correct(update, before_elements):
    is_correct = True

    for index, rule in enumerate(update):
        for i in range(index):
            if rule in before_elements[i]:
                is_correct = False
                break
    
    return is_correct


def topological_sort(update, updates_rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for rule in update:
        in_degree[rule] = 0

    for (bef, after) in updates_rules:
        if after in update and bef in update:
            graph[bef].append(after)
            in_degree[after] += 1

    zero_in_degree = deque([node for node in update if in_degree[node] == 0])

    update.clear()

    while zero_in_degree:
        current = zero_in_degree.popleft()
        update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)


if __name__ == "__main__":
    main()