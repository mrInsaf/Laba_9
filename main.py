class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


class Bishop(Figure):
    def move(self, x, y):
        self.set_x(x)
        self.set_y(y)


        