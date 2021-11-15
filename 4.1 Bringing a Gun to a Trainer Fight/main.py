"""
Hard to explain without a drawing.
In short, hitting the target by having the laser bounce of a wall is equivalent of shooting in straight line, with the same length, into a reflected room.
This solution generates reflected rooms, in order, and for each checks if the target reflection can be shot without hitting any obstacle.
Obstacle being the original target, original position, and all previous reflections of both.
We do that by simply checking the shooting angle with atan2.
Finally, there is a finite number of rooms to check, which can be calculated using the gun range and the room size.
"""

import math

TOP = 1
RIGHT = 2
BOTTOM = 3
LEFT = 4


def next_direction(d):
    return TOP if d == 4 else d+1


def solution(dimensions, origin, target, r):
    hits = 0
    angles = []
    rooms_to_check = number_of_rooms_to_check(dimensions, origin, r)

    for reflected_origin, reflected_target in reflected_rooms(dimensions, origin, target):

        if distance(origin, reflected_target) <= r:

            origin_angle = shooting_angle(origin, reflected_origin)
            if hits > 0:  # Skip first round
                angles.append(origin_angle)

            target_angle = shooting_angle(origin, reflected_target)

            if target_angle not in angles:
                angles.append(target_angle)
                hits += 1

        rooms_to_check -= 1
        if rooms_to_check == 0:
            break

    return hits


def number_of_rooms_to_check(dimensions, origin, r):
    max_required_rooms_in_straight_line = max(
        dimensions[0] // r,
        dimensions[1] // r,
        r // dimensions[0],
        r // dimensions[1]
    )
    return (max_required_rooms_in_straight_line * 2 + 3) ** 2


def reflected_rooms(d, origin, target):
    o = origin
    t = target
    reflection_axis = LEFT
    required_reflections = 0
    reps = 0
    offset = (0, 0)

    while True:
        yield (o, t)

        reflection_axis, required_reflections, reps = next_reflection_axis(
            reflection_axis, required_reflections, reps
        )

        ox = oy = 0
        if reflection_axis == TOP:
            oy = d[1]
        elif reflection_axis == BOTTOM:
            oy = -d[1]
        elif reflection_axis == RIGHT:
            ox = d[0]
        elif reflection_axis == LEFT:
            ox = -d[0]
        offset = offset[0]+ox, offset[1]+oy

        origin, target = reflect_room(d, origin, target, reflection_axis)
        o, t = [offset_point(p, offset) for p in (origin, target)]


def next_reflection_axis(reflection_axis, requirement, reps):
    if reps == requirement:
        next_axis = next_direction(reflection_axis)
        if reflection_axis == LEFT and next_axis == TOP:
            requirement += 1
        if reflection_axis == RIGHT and next_axis == BOTTOM:
            requirement += 1

        reflection_axis = next_axis
        reps = 0

    return reflection_axis, requirement, reps+1


def reflect_room(d, origin, target, rd):
    o = reflect_point(d, origin, rd)
    t = reflect_point(d, target, rd)
    return o, t


def reflect_point(dimensions, p, reflect_direction):
    x, y = p
    w, h = dimensions

    if reflect_direction in [TOP, BOTTOM]:
        return x, h - y
    else:
        return w - x, y


def offset_point(p, o):
    return p[0]+o[0], p[1]+o[1]


def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def shooting_angle(o, p):
    return math.atan2(o[1]-p[1], p[0]-o[0])
