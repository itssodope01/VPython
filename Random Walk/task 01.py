import random
import time

left_wall = -15
right_wall = 15
position = 0
flips = 0


def flip_coin():
    return random.choice([-1, 1])

def display_position(position, left_wall, right_wall):

    line = [' '] * (right_wall - left_wall + 1)
    line[position - left_wall] = '*'
    print('|' + ''.join(line) + '|' + '  ' +  str(position))


print("\n"' ' + ' '*15 + 'START' + ' '*15 + ' ')
print("\n"'|' + ' '*15 + '*' + ' '*15 + '|' + '  ' +  str(0))

while position > left_wall and position < right_wall:
    position += flip_coin()
    flips += 1

    display_position(position, left_wall, right_wall)

    time.sleep(0.03)

print(f"Total coin flips: {flips}")
