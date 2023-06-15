from classes_and_functions import *

figures = []

while True:
    inp = int(input(
        'Выберите желаемое действие\n [1] - Вывести текущую доску\n [2] - Добавить фигуру\n [3] - Переместить фигуру\n'))
    if inp == 1:
        print('Текущая доска: \n')
        print_chessboard(figures)
        print()
    if inp == 2:
        inp_2 = int(input('Добавить\n [1] - Слона, [2] - Просто фигуру\n'))
        x, y = input_coors()


        if inp_2 == 1:
            new_bishop = Bishop(x, y)
            figures.append(new_bishop)
        elif inp_2 == 2:
            new_figure = Figure(x, y)
            figures.append(new_figure)

    if inp == 3:
        print('Введите координаты фигуры, которую хотите передвинуть\n')
        start_x, start_y = input_coors()
        print('\nКуда передвинуть?\n')
        dest_x, dest_y = input_coors()

