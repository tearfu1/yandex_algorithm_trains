t, d, n = map(int, input().split())
start_pos = (0, 0)
current_positions = [start_pos]

for i in range(n):
    x, y = map(int, input().split())
    next_positions = set()
    for position in current_positions:
        next_positions.add(position)

        next_position = (position[0] - 1, position[1])
        next_positions.add(next_position)

        next_position = (position[0], position[1] - 1)
        next_positions.add(next_position)

        next_position = (position[0] + 1, position[1])
        next_positions.add(next_position)

        next_position = (position[0], position[1] + 1)
        next_positions.add(next_position)

    for minute in range(t - 1):
        i = 0
        new_next_positions = set()
        for position in next_positions:
            new_next_positions.add(position)

            next_position = (position[0] - 1, position[1])
            new_next_positions.add(next_position)

            next_position = (position[0], position[1] - 1)
            new_next_positions.add(next_position)

            next_position = (position[0] + 1, position[1])
            new_next_positions.add(next_position)

            next_position = (position[0], position[1] + 1)
            new_next_positions.add(next_position)
        next_positions = new_next_positions

    good_positions = []
    for position in next_positions:
        if abs(position[0] - x) + abs(position[1] - y) <= d:
            if position not in good_positions:
                good_positions.append(position)

    current_positions = good_positions

print(len(current_positions))
for point in current_positions:
    print(*point)
