## Inspired from: https://github.com/Cdawn99/AoC2024/blob/master/Day13/day13_p2.py

import numpy as np
from numpy.linalg import solve

def main():
    with open("day13/13-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    count = 0

    ax = 0
    ay = 0
    bx = 0
    by = 0
    fx = 0
    fy = 0

    for line_ in data:
        if (line_ == ""):
            continue

        line = line_.split(" ")
        if line[0] == "Button" and line[1] == "A:":
            ax = int(line[2][2:line[2].index(",")])
            ay = int(line[3][2:])
        elif line[0] == "Button" and line[1] == "B:":
            bx = int(line[2][2:line[2].index(",")])
            by = int(line[3][2:])
        else:
            fx = int(line[1][2:line[1].index(",")])
            fy = int(line[2][2:])

        if (ax != 0) and (bx != 0) and (fx != 0):
            res = process((ax, ay), (bx, by), (fx + 10000000000000, fy + 10000000000000))
            if (res is not None):
                count += res
            ax = 0
            ay = 0
            bx = 0
            by = 0
            fx = 0
            fy = 0
    
    print(round(count))

def process(a_button, b_button, f_dest):
    AB = np.column_stack((a_button, b_button))

    solution = np.rint(solve(AB, f_dest))
    if np.all(AB @ solution == f_dest):
        a, b = solution
        return 3 * a + b

    return None

if __name__ == "__main__":
    main()