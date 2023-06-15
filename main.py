class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_coordinates(self):
        print(self.x, self.y)
        return self.x, self.y

    def move(self, dest_x, dest_y):
        self.set_x(dest_x)
        self.set_y(dest_y)

    def raise_error(self):
        print(f'Введите корректные данные для класса {self.__class__.__name__}')


class Bishop(Figure):
    def move(self, dest_x, dest_y):
        if abs(self.x - dest_x) == abs(self.y - dest_y):
            super().move(dest_x, dest_y)
        else:
            self.raise_error()


my_bishop = Bishop(6, 6)
my_bishop.get_coordinates()
my_bishop.move(6, 7)
my_bishop.get_coordinates()




