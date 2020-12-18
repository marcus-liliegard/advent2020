from day12_data import data

navigation_list = [(s[0:1], int(s[1:])) for s in data.split('\n')]


# part one
def follow_actions(start_direction, navigation):
    direction = start_direction
    coordinates = [0, 0]

    for action, value in navigation:

        if action == 'N' or (action == 'F' and direction == 270):
            coordinates[1] += value
        elif action == 'S' or (action == 'F' and direction == 90):
            coordinates[1] -= value
        elif action == 'E' or (action == 'F' and direction == 0):
            coordinates[0] += value
        elif action == 'W' or (action == 'F' and direction == 180):
            coordinates[0] -= value
        elif action == 'L':
            direction -= value
            if direction < 0:
                direction += 360
        elif action == 'R':
            direction += value
            if direction >= 360:
                direction -= 360

    return coordinates


end_coordinates = follow_actions(0, navigation_list)
print(sum(map(abs, end_coordinates)))


# part two
def waypoint_navigation(start_waypoint, navigation):
    waypoint = start_waypoint
    coordinates = [0, 0]

    for action, value in navigation:
        if action == 'N':
            waypoint[1] += value
        elif action == 'S':
            waypoint[1] -= value
        elif action == 'E':
            waypoint[0] += value
        elif action == 'W':
            waypoint[0] -= value
        elif action in ['L', 'R']:
            if (action == 'L' and value == 90) or (action == 'R' and value == 270):
                waypoint = [-waypoint[1], waypoint[0]]
            elif (action == 'L' and value == 180) or (action == 'R' and value == 180):
                waypoint = [-waypoint[0], -waypoint[1]]
            elif (action == 'L' and value == 270) or (action == 'R' and value == 90):
                waypoint = [waypoint[1], -waypoint[0]]
        elif action == 'F':
            coordinates[0] += waypoint[0] * value
            coordinates[1] += waypoint[1] * value

    return coordinates


end_coordinates = waypoint_navigation([10, 1], navigation_list)
print(sum(map(abs, end_coordinates)))
