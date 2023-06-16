from classes_and_functions import *

figures = []

while True:
    inp = input(
        'Выберите желаемое действие\n [1] - Вывести текущую доску\n [2] - Добавить фигуру\n [3] - Переместить фигуру\n')

    if inp == '1':
        print('Текущая доска: \n')
        print_chessboard(figures)
        print()

    if inp == '2':
        inp_2 = int(input('Добавить\n [1] - Слона, [2] - Просто фигуру\n'))
        while True:
            x, y, flag = input_coors(figures)
            if flag:
                print('Эта клетка занята!')
                continue
            elif inp_2 == 1:
                new_bishop = Bishop(x, y)
                figures.append(new_bishop)
                break
            elif inp_2 == 2:
                new_figure = Figure(x, y)
                figures.append(new_figure)
                break

    if inp == '3':
        print('Введите координаты фигуры, которую хотите передвинуть\n')

        while True:
            start_x, start_y, flag = input_coors(figures)
            if not flag:
                print('Фигуры с этими координатами нет')
                continue
            else:
                break

        print('Куда передвинуть?')

        while True:
            dest_x, dest_y, flag = input_coors(figures)
            if flag:
                print('Эта клетка уже занята!')
                continue
            else:
                if move_smth(start_x, start_y, dest_x, dest_y, figures):
                    break
                else:
                    continue

    else:
        continue

