from termcolor import cprint


def checking(game):
    """
    Позволит проверять есть ли победитель
    :param game:
    :return:
    """
    if game[0][0] == 'X' and game[0][1] == 'X' and game[0][2] == 'X':
        cprint('player 1 won!', 'yellow')
        return 1
    elif game[0][0] == 'O' and game[0][1] == 'O' and game[0][2] == 'O':
        cprint('player 2 won!', 'yellow')  # 1-я строка
        return 1
    elif game[1][0] == 'X' and game[1][1] == 'X' and game[1][2] == 'X':
        cprint('player 1 won!', 'yellow')
        return 1
    elif game[1][0] == 'O' and game[1][1] == 'O' and game[1][2] == 'O':
        cprint('player 2 won!', 'yellow')  # 2-я строка
        return 1
    elif game[2][0] == 'X' and game[2][1] == 'X' and game[2][2] == 'X':
        cprint('player 1 won!', 'yellow')
        p = 1
    elif game[2][0] == 'O' and game[2][1] == 'O' and game[2][2] == 'O':
        cprint('player 2 won!', 'yellow')  # 3-я строка
        return 1
    elif game[0][0] == 'X' and game[1][0] == 'X' and game[2][0] == 'X':
        cprint('player 1 won!', 'yellow')
        return 1
    elif game[0][0] == 'O' and game[1][0] == 'O' and game[2][0] == 'O':
        cprint('player 2 won!', 'yellow')  # 1-й столбец
        return 1
    elif game[0][1] == 'X' and game[1][1] == 'X' and game[2][1] == 'X':
        cprint('player 1 won!', 'yellow')
        return 1
    elif game[0][1] == 'O' and game[1][1] == 'O' and game[2][1] == 'O':
        cprint('player 2 won!', 'yellow')  # 2-й столбец
        return 1
    elif game[0][2] == 'X' and game[1][2] == 'X' and game[2][2] == 'X':
        cprint('player 1 won!', 'yellow')
        return 1
    elif game[0][2] == 'O' and game[1][2] == 'O' and game[2][2] == 'O':
        cprint('player 2 won!', 'yellow')  # 3-й столбец
        return 1
    elif game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        cprint('player 1 won!', 'yellow')
        return 1
    elif game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        cprint('player 2 won!', 'yellow')  # 1-диагональ
        return 1
    elif game[0][2] == 'X' and game[1][1] == 'X' and game[2][0] == 'X':
        cprint('player 1 won!', 'yellow')
        return 1
    elif game[0][2] == 'O' and game[1][1] == 'O' and game[2][0] == 'O':
        cprint('player 2 won!', 'yellow')  # 2-диагональ
        return 1


def draw(a):
    print('\n    A  B  C')
    for i in range(len(a)):
        print(i + 1, '[', end='')
        for j in range(len(a[i])):
            print(a[i][j].center(3), end='')
        print(']')


a = [['*', '*', '*'],
     ['*', '*', '*'],
     ['*', '*', '*']]

draw(a)

while True:
    print('\nPlayer 1')
    p1 = input('Position 1: ').upper().strip()
    if p1 == 'EXIT':
        print('\nThank you for game!')
        break
    p2 = input('Position 2: ').strip()
    if p1 == 'A':
        if p2 == '1':
            if a[0][0] != 'O':
                a[0][0] = 'X'
        elif p2 == '2':
            if a[1][0] != 'O':
                a[1][0] = 'X'
        elif p2 == '3':
            if a[2][0] != 'O':
                a[2][0] = 'X'
    elif p1 == 'B':
        if p2 == '1':
            if a[0][1] != 'O':
                a[0][1] = 'X'
        elif p2 == '2':
            if a[1][1] != 'O':
                a[1][1] = 'X'
        elif p2 == '3':
            if a[2][1] != 'O':
                a[2][1] = 'X'
    elif p1 == 'C':
        if p2 == '1':
            if a[0][2] != 'O':
                a[0][2] = 'X'
        elif p2 == '2':
            if a[1][2] != 'O':
                a[1][2] = 'X'
        elif p2 == '3':
            if a[2][2] != 'O':
                a[2][2] = 'X'

    draw(a)
    if checking(a) == 1:
        break

    print('\nPlayer 2')
    p1 = input('Position 1: ').upper().strip()
    if p1 == 'EXIT':
        print('\nThank you for game!')
        break
    p2 = input('Position 2: ').strip()
    if p1 == 'A':
        if p2 == '1':
            if a[0][0] != 'X':
                a[0][0] = 'O'
        elif p2 == '2':
            if a[1][0] != 'X':
                a[1][0] = 'O'
        elif p2 == '3':
            if a[2][0] != 'X':
                a[2][0] = 'O'
    elif p1 == 'B':
        if p2 == '1':
            if a[0][1] != 'X':
                a[0][1] = 'O'
        elif p2 == '2':
            if a[1][1] != 'X':
                a[1][1] = 'O'
        elif p2 == '3':
            if a[2][1] != 'X':
                a[2][1] = 'O'
    elif p1 == 'C':
        if p2 == '1':
            if a[0][2] != 'X':
                a[0][2] = 'O'
        elif p2 == '2':
            if a[1][2] != 'X':
                a[1][2] = 'O'
        elif p2 == '3':
            if a[2][2] != 'X':
                a[2][2] = 'O'

    draw(a)

    if checking(a) == 1:
        break