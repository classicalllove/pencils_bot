import random

print('How many pencils would you like to use: ')

while True:
    try:
        number_of_pencils = int(input())
        if number_of_pencils == 0:
            print('The number of pencils should be positive')
        elif number_of_pencils < 0:
            print('The number of pencils should be numeric')
        else:
            break
    except ValueError:
        print('The number of pencils should be numeric')

name = input('Who will be the first (John, Jack): ')

while True:
    if name != 'John' and name != 'Jack':
        print('Choose between John and Jack')
        name = input()
        continue
    else:
        break


def opponent(name):
    if name == 'John':
        return 'Jack'
    else:
        return 'John'


while number_of_pencils > 0:
    print('|' * number_of_pencils)
    if name == 'Jack':
        turn_1 = "{}'s turn:".format(name)
        print(turn_1)
    if name == 'John':
        turn_1 = "{}'s turn!".format(name)
        print(turn_1)
    while True:
        try:
            if name == 'John':
                pen_count = int(input())
            else:
                pen_count = 0
                if number_of_pencils == 1:
                    pen_count = 1
                elif number_of_pencils % 4 == 1:
                    pen_count = random.randint(1, 3)
                elif number_of_pencils % 4 == 0:
                    pen_count = 3
                elif number_of_pencils % 4 == 3:
                    pen_count = 2
                elif number_of_pencils % 4 == 2:
                    pen_count = 1
                print(pen_count)
        except ValueError:
            print("Possible values: '1', '2' or '3'")
            continue
        if pen_count == 1 or pen_count == 2 or pen_count == 3:
            if pen_count > number_of_pencils:
                print('Too many pencils were taken')
            else:
                name = opponent(name)
                number_of_pencils -= pen_count
                if number_of_pencils == 0:
                    print(f'{name} won!')
                    break
                else:
                    print('|' * number_of_pencils)
                    turn_1 = "{}'s turn!".format(name)
                    print(turn_1)
                    continue
        else:
            print("Possible values: '1', '2' or '3'")
            continue
