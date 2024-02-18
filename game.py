import random
import msvcrt
import os
x_kapik = random.randint(1,18)
y_kapik = random.randint(1,18)
x_banan = random.randint(2,17)
y_banan = random.randint(2,17)
x_odz = random.randint(2,17)
y_odz = random.randint(2,17)

point = 0
live = 3
map_x = 20
map_y = 20

while True:
    os.system('cls')
    for i in range(1,map_x):
        for j in range(1,map_y):
            if i == 1 or i == 19 or j == 1 or j == 19:
                print('🌵', end='')
            elif x_kapik == i and y_kapik == j: 
                print('🦍', end='')
            elif x_banan == i and y_banan == j:
                print('🍌', end='')
            elif i != 1 or i != 19:
                print('🌴', end='')
        print()
    if x_banan == x_kapik and y_banan == y_kapik:
        point += 1
        x_banan = random.randint(2,17)
        y_banan = random.randint(2,17)
        if point == 3:
            print('You WIN')
            break
    if x_kapik == map_x-1 or y_kapik == map_y-1  or y_kapik == 1 or x_kapik == 1 or x_kapik == x_odz and y_kapik == y_odz:
        live -= 1
        if live == 0:
            print('You Lose')
            break
    print(f'live: {live}')
    print(f'point: {point}')
    




    step = msvcrt.getwch().lower()
    control = step
    n = 0
    if step == '0':
        break
    if step in ('w','a','s','d'):
        for step in ('w','a','s','d'):
            n += 1
            if control == step:
                break
        if n == 1 and x_kapik != 20:
            x_kapik -= 1
        elif n == 2 and y_kapik != -1 :
            y_kapik -= 1
        elif n == 3 and x_kapik != -1 :
            x_kapik += 1
        elif n == 4 and y_kapik != 20:
            y_kapik += 1
