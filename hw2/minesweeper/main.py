def makefield(n, m, coords):
    di = [1, 1, 1, 0, 0, -1, -1, -1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    field = [[0 for _ in range(m + 2)] for _ in range(n + 2)]

    for minx, miny in coords:
        for k in range(len(di)):
            field[minx + di[k]][miny + dj[k]] += 1

    for minx, miny in coords:
        field[minx][miny] = "*"

    field = field[1: len(field) - 1]
    for i in range(len(field)):
        field[i] = field[i][1: len(field[i]) - 1]
    return field


def main():
    n, m, k = map(int, input().split())
    coords = []
    for i in range(k):
        coords.append(tuple(map(int, input().split())))
    field = makefield(n, m, coords)
    for i in field:
        print(*i)


main()
