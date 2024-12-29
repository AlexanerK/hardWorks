import math
from typing import get_args


class Figure:
    sides_count = 0
    def __init__(self, color, sides, filled = True):
        self.__sides = [sides]
        if len(self.__sides) == self.sides_count:
            self.__sides = [sides]
        else:
            if self.sides_count == 12 and len(self.__sides) == 1 :
                self.__sides = self.__sides * self.sides_count
            else:
                self.__sides = [1] * self.sides_count
                return self.__sides
        self.__color = color
        self.filled = filled


    def get_color(self):

        if self.__is_valid_color() == False:
            print(f'Введены значения цветов не в интервале от 0 до 255')
        return f'Список цветов: {self.__color}'

    def __is_valid_color(self):
        if (0 < self.r <= 255 and 0 < self.g <= 255 and 0 < self.b <= 255
                and self.r % 1 == 0  and self.g % 1 ==0 and self.b % 1 == 0) :
            return True
        else:
            return False

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        rgb_color = [r, g, b]
        if self.__is_valid_color() == True:
            self.__color = rgb_color

    def __is_valid_sides(self):
        if all(isinstance(item,int) for item in self.new_sides) and len(self.new_sides) == self.sides_count :
            return True
        else: False

    def get_sides(self):
        d = self.__sides
        return self.__sides



    def __len__(self):
        perimetr = 0
        for i in self.__sides:
            perimetr += i
        return perimetr

    def set_sides(self, *new_sides):
        self.new_sides = [*new_sides]
        if len(self.new_sides) == self.sides_count :
            self.__sides = self.new_sides



            #self.__sides = [self.new_sides[0] * self.sides_count]


class Circle(Figure):

    sides_count = 1
    def radius(self):
        self.__radius = self.__len__() /(2*3.14)
        return self.__radius

    def get_square(self):
        return 3.14 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        self.square = math.sqrt((self.__len__() / 2) * ((self.__len__() / 2) - self._Figure__sides[0]) *
                               ((self.__len__() / 2) - self._Figure__sides[1])*((self.__len__() / 2) - self._Figure__sides[2]))
        return  self.square

class Cube(Figure):
    sides_count = 12
    volume = 0
    def get_volume(self):
        volume = self._Figure__sides[0] ** 3
        return volume



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())