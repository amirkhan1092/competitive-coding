def main():
    size = int(input())
    cell = input().split()

    for i in range(0, len(cell)):
        cell[i] = int(cell[i])
    m = -1
    j = 0
    cycle = []
    for i in range(0, 23):
        if m == 2:
            if cycle[0] == cycle[-1]:
                return sum(cycle[:-1])
            else:
                return 0
        else:
            cycle.append(cell[j])
            j = cell[j]
    else:
        return 0

main()
