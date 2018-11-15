# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    def __init__(self, A, B, C):
        def length(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C
        self.AB = length(self.A, self.B)
        self.BC = length(self.B, self.C)
        self.AC = length(self.C, self.A)

    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2

        return math.sqrt(
            semi_perimeter * (semi_perimeter - self.AB) * (semi_perimeter - self.BC) * (semi_perimeter - self.AC))

    def perimeterTriangle(self):
        return self.AB + self.BC + self.AC

    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)


tr = Triangle((0, 0), (1, 0), (0, 1))

print(tr.areaTriangle())
print(tr.heightTriangle())
print(tr.perimeterTriangle())



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
import math
class Trapeze:
    def __init__(self, A, B, C, D):
        # Функция вычисляет длину стороны согласно координатам точек
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)

        def areaTriangle(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2
            return math.sqrt(semi_perimeter * (semi_perimeter - len1) * (semi_perimeter - len2) * (semi_perimeter - len3))

        self.A = A
        self.B = B
        self.C = C
        self.D = D
        #длины сторон
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CD = sideLen(self.C, self.D)
        self.DA = sideLen(self.D, self.A)
        self.diagonal_AC = sideLen(self.C, self.A)
        self.diagonal_BD = sideLen(self.B, self.D)
        #Периметр
        self.perimeter = self.AB + self.BC + self.CD + self.DA
        #Площадь
        self.area = areaTriangle(self.AB, self.diagonal_BD, self.DA) + areaTriangle(self.diagonal_BD, self.BC, self.CD)
        #Проверка на равнобочность
    def isTrapezeEqu(self):
        if self.diagonal_AC == self.diagonal_BD:
            return True
        return False


trapezium = Trapeze((0, 0), (3, 0), (2, 1), (1, 2))

print(trapezium.perimeter)
print(trapezium.area)
print(trapezium.isTrapezeEqu())
