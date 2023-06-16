letters = "_ABCDEFGH"
class Figure:

    def __init__(self, x, y):
        self.y = y
        self.x = letters.find(x)

    def __set_x(self, x):
        self.x = letters.find(x)

    def __set_y(self, y):
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def move(self, dest_x, dest_y):
        self.__set_x(dest_x)
        self.__set_y(dest_y)
        return True

    def raise_error(self):
        print(f'Введите корректные данные для класса {self.__class__.__name__}')


class Bishop(Figure):
    def move(self, dest_x, dest_y):
        if abs(self.x - letters.find(dest_x)) == abs(self.y - dest_y):
            super().move(dest_x, dest_y)
            return True
        else:
            self.raise_error()
            return False


def print_chessboard(figures):
    size = 8
    letters = "ABCDEFGH"  # Список букв для отображения столбцов
    for row in range(size, 0, -1):  # Изменяем порядок вывода строк снизу вверх
        print(row, end="  ")  # Выводим цифру строки
        for col in range(1, 9):
            for figure in figures:
                coor = figure.get_coordinates()
                if row == coor[1] and col == coor[0]:
                    if figure.__class__.__name__ == 'Bishop':
                        print('♗', end="  ")
                    else:
                        print('*', end="  ")
                    break
            else:
                if (row + col) % 2 == 0:
                    print("■", end="  ")
                else:
                    print("□", end="  ")
        print()
    print("   ", end="")  # Выводим пробелы перед буквами столбцов
    for col in range(size):
        print(letters[col], end="  ")  # Выводим букву столбца
    print()


def input_coors(figures):
    flag = False
    while True:
        coors = input('Введите координаты фигуры, например, A2 или F8\n')

        if len(coors) != 2:
            print('\nКоличество координат должно быть 2!')
            continue

        x = coors[0]
        y = int(coors[1])
        for figure in figures:
            fig_x, fig_y = figure.get_coordinates()
            if letters[fig_x] == x and fig_y == y:
                flag = True
                break

        if x not in letters:
            print('Первая координата должна быть A-H')
            continue  # Возвращаемся к вводу координат
        elif y not in range(1, 9):
            print("Вторая координата должна быть 1-8")
            continue  # Возвращаемся к вводу координат

        else:
            return x, y, flag

def move_smth(start_x, start_y, dest_x, dest_y, figures):
    for figure in figures:
        x, y = figure.get_coordinates()
        if start_x == letters[x] and start_y == y:
            if not figure.move(dest_x, dest_y):
                return False
            else:
                print(f'Переместил {figure.__class__.__name__} {start_x}{start_y}-->{dest_x}{dest_y}')
                return True
