class BoardException(Exception):     # общий класс исключений
    pass
class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"
class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"
class BoardWrongShipException(BoardException):              # исключение ошибочного размещения корабля
    pass

class Dot:    # класс создания точки
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y     # метод сравнения точек
    def __repr__(self):
        return f'Dot({self.x},{self.y})'    # метод вывода точки в консоль

class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l
    @property # декоратор  метода свойства корабля
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y
            if self.o == 0:
                cur_x += i
            elif self.o == 1:
                cur_y += i
            ship_dots.append(Dot(cur_x,cur_y))
        return ship_dots
    def shooten(self,shot):    # метод попадания в корабль
        return shot in self.dots
class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid    # сокрытие игрового поля

        self.count = 0    # переменная колличества пораженных кораблей

        self.field = [['0']*size for _ in range(size)]    # атрибут состояния клеточек поля

        self.bysy = []   # занятые точки

        self.ships = []   # список кораблей доски

    def __str__(self):
        res = ""
        res += " | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | "  .join(row) + " |"

        if self.hid:
            res = res.replace("■", "0")
        return res
b = Board()
print(b)
