import math

SQUARE_TO_GET = 23


bottom_right_corner_of_base_square = SQUARE_TO_GET
closest_whole_root = math.sqrt(float(bottom_right_corner_of_base_square))

while bottom_right_corner_of_base_square > 0 and (int(closest_whole_root) != closest_whole_root
                                    or bottom_right_corner_of_base_square % 2 == 0):
    bottom_right_corner_of_base_square -= 1
    closest_whole_root = math.sqrt(float(bottom_right_corner_of_base_square))

# 1          10                 9
difference = SQUARE_TO_GET - bottom_right_corner_of_base_square
# 3
base_length = math.sqrt(bottom_right_corner_of_base_square)
# 1
mod = SQUARE_TO_GET % math.sqrt(bottom_right_corner_of_base_square)
mod1_x = (difference + base_length) % base_length + 1
mod1_y = (difference + base_length) % (base_length + 1)

# 2
div = math.ceil(difference / base_length)
side = math.ceil(difference / (base_length + 1))

# base_length       3  3  3 |  3 |  3  3  3 |  3 |  3  3  3 |  3 |  3  3  3
# highest_position 10 11 12 | 13 | 14 15 16 | 17 | 18 19 20 | 21 | 22 23 24
# bottom_right      9  9  9 |  9 |  9  9  9 |  9 |  9  9  9 |  9 |  9  9  9
# --------------------------|----|----------|----|----------|----|---------
# difference        1  2  3 |  4 |  5  6  7 |  8 |  9 10 11 | 12 | 13 14 15
# mod1              0  1  2 |  3 |  0  1  2 |  3 |  0  1  2 |  3 |  0  1  2
# side              1  1  1 |  1 |  2  2  2 |  2 |  3  3  3 |  3 |  4  4  4
# --------------------------|----|----------|----|----------|----|---------
# x in terms of b  +1 +1 +1 | +1 |  0 -1 -2 | -3 | -3 -3 -3 | -3 | -2 -1  0
# y in terms of b   0 -1 -2 | -3 | -3 -3 -3 | -3 | -2 -1  0 | +1 | +1 +1 +1

# switch side
# case 1: x = b + 1                     y = b - mod1
# case 2: x = b - mod1                  y = b - base_length
# case 3: x = b - base_length           y = b - (base_length - mod1)
# case 4: x = b - (base_length - mod1)  y = b + 1

# x = b + side==1 - (side==2)*(mod1) - (side==3)*(base_length) - (side==4)*(base_length - mod1)
# y = b + side==4 - (side==1)*(mod1) - (side==2)*(base_length) - (side==3)*(base_length - mod1)

# x_distance = abs(
#     int(math.floor((float(spiral_width) - 1)/2)
#     - b + side==1 - (side==2)*(mod1) - (side==3)*(base_length) - (side==4)*(base_length - mod1)
# )
# y_distance = abs(
#     int(math.ceil((float(spiral_height) - 1)/2))
#     - b + side==4 - (side==1)*(mod1) - (side==2)*(base_length) - (side==3)*(base_length - mod1)
# )

# result = abs(
#     int(math.floor((float(spiral_width) - 1)/2)
#     - b + side==1 - (side==2)*(mod1) - (side==3)*(base_length) - (side==4)*(base_length - mod1)
# ) + abs(
#     int(math.ceil((float(spiral_height) - 1)/2))
#     - b + side==4 - (side==1)*(mod1) - (side==2)*(base_length) - (side==3)*(base_length - mod1)
# )

print bottom_right_corner_of_base_square

if not difference:                        # if difference == 0
    spiral_width, spiral_height = base_length, base_length
elif difference <= base_length + 1:       # if 0 < difference <= base_length + 1 ... 0 < 3 <= 3
    spiral_width, spiral_height =  base_length + 1, base_length
elif difference <= 2 * (base_length + 1): # if base_length + 1 < difference <= 2 * (base_length + 1)
    spiral_width, spiral_height =  base_length + 1, base_length + 1
elif difference <= 3 * (base_length + 1): # if 2 * (base_length + 1) < difference <= 3 * (base_length + 1)
    spiral_width, spiral_height =  base_length + 2, base_length + 1
else:                                     # if 3 * (base_length + 1) < difference
    spiral_width, spiral_height =  base_length + 2, base_length + 2

centre_x = int(math.floor((float(spiral_width) - 1)/2))
centre_y = int(math.ceil((float(spiral_height) - 1)/2))

print "centre"
print centre_x
print centre_y
print

b_x = math.floor(centre_x + base_length / 2)
b_y = math.floor(centre_y + base_length / 2)

print "b"
print b_x
print b_y
print

pos_x = (b_x + ((side==1)*1) - ((side==2)*(mod1_x)) - ((side==3)*(base_length)) - ((side==4)*(base_length - mod1_x)))
pos_y = (b_y + ((side==4)*1) - ((side==1)*(mod1_y)) - ((side==2)*(base_length)) - ((side==3)*(base_length - mod1_y)))

print b_x
print ((side==1)*1)
# print ((side==2)*(mod1))
print ((side==3)*(base_length))
# print ((side==4)*(base_length - mod1)) # sb 1
print

print
print base_length
# print mod1
# print base_length - mod1
print

print "pos"
print pos_x # sb 2
print pos_y
print

x_distance = abs(centre_x - pos_x)
y_distance = abs(centre_y - pos_y)

print x_distance
print y_distance

result = int(x_distance + y_distance)

print result
