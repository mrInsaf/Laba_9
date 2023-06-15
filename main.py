class Figure:

    letters = "ABCDEFGH"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __set_x(self, x):
        self.x = x

    def __set_y(self, y):
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def move(self, dest_x, dest_y):
        self.__set_x(dest_x)
        self.__set_y(dest_y)

    def raise_error(self):
        print(f'Введите корректные данные для класса {self.__class__.__name__}')


class Bishop(Figure):
    def move(self, dest_x, dest_y):
        if abs(self.x - dest_x) == abs(self.y - dest_y):
            super().move(dest_x, dest_y)
        else:
            self.raise_error()


def print_chessboard(figures):
    size = 8
    letters = "ABCDEFGH"  # Список букв для отображения столбцов
    for row in range(size - 1, -1, -1):  # Изменяем порядок вывода строк снизу вверх
        print(row + 1, end="  ")  # Выводим цифру строки
        for col in range(size):
            for figure in figures:
                coor = figure.get_coordinates()
                if row == coor[0] and col == coor[1]:
                    if figure.__class__.__name__ == 'Bishop':
                        print('B', end="  ")
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




figures = []




my_bishop = Bishop(6, 6)


figures.append(my_bishop)
figures[0].move(4, 7)
print(figures[0].get_coordinates())
# print(len(figures))

print_chessboard(figures)  # Выводит подобие шахматной доски 8x8

