import math

SQUARE_TO_GET = 277678

# x x x x x x x
# x x x x x x x
# x x x x x x x
# x x x o x x x
# x x x x x x x
# x x x x x X x
# X

# max_pos = 4
# difference = 18, 19, 20, 21, 22, 23, 24
# difference % (max_pos + 2) = 0, 1, 2, 3, 4, 5, 0
# (max_pos + 1) - (difference % (max_pos + 2)) = 5, 4, 3, 2, 1, 0
# x, y = 1, 0

def get_spiral_shape(highest_position):
    position_to_check = highest_position
    closest_whole_root = math.sqrt(float(position_to_check))

    while position_to_check > 0 and (int(closest_whole_root) != closest_whole_root
                                     or position_to_check % 2 == 0):
        position_to_check -= 1
        closest_whole_root = math.sqrt(float(position_to_check))

    difference = highest_position - position_to_check
    base_length = math.sqrt(position_to_check)

    print position_to_check

    if not difference:
        return base_length, base_length
    elif difference <= base_length + 1:
        return base_length + 1, base_length
    elif difference <= 2 * (base_length + 1):
        return base_length + 1, base_length + 1
    elif difference <= 3 * (base_length + 1):
        return base_length + 2, base_length + 1
    else:
        return base_length + 2, base_length + 2


def get_spiral_centre(spiral_width, spiral_height):
    return (int(math.floor((float(spiral_width) - 1)/2)),
            int(math.ceil((float(spiral_height) - 1)/2)))


def get_position_of_square_in_spiral(square):
    position_to_check = square
    closest_whole_root = math.sqrt(float(position_to_check))

    while position_to_check > 0 and (int(closest_whole_root) != closest_whole_root
                                     or position_to_check % 2 == 0):
        position_to_check -= 1
        closest_whole_root = math.sqrt(float(position_to_check))

    difference = square - position_to_check
    max_pos = math.sqrt(position_to_check) - 1

    bottom_right_corner = position_to_check

    if not difference:
        return max_pos, max_pos
    elif difference <= max_pos + 1:
        return max_pos + 1, max_pos + 1 - difference
    elif difference <= 2 * (max_pos + 1) + 1:
        return max_pos + 1 - (difference % (max_pos + 2)), 0
    elif difference <= 3 * (max_pos + 1) + 2:
        return 0, (max_pos + 1) - (difference % (max_pos + 2))
    elif difference <= 4 * (max_pos + 1) + 3:
        return difference % (max_pos + 2), max_pos + 2
    else:
        return max_pos + 2, max_pos + 2



def get_distance_to_spiral_centre(spiral_centre_x, spiral_centre_y, pos_x, pos_y):
    return abs(spiral_centre_x - pos_x) + abs(spiral_centre_y - pos_y)


# get spiral shape
width, height = get_spiral_shape(SQUARE_TO_GET)
print width
print height

# get centre of spiral
centre_x, centre_y = get_spiral_centre(width, height)
print centre_x
print centre_y

# get position of square in spiral
pos_x, pos_y = get_position_of_square_in_spiral(SQUARE_TO_GET)
print pos_x
print pos_y

# find distance from square to centre
print get_distance_to_spiral_centre(centre_x, centre_y, pos_x, pos_y)
