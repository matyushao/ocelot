"""
Задача 1

Создайте класс Soda (для определения типа газированной воды),
принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
В этом классе реализуйте метод show_my_drink(), выводящий на печать Газировка и {ДОБАВКА}
в случае наличия добавки, а иначе отобразится следующая фраза: Обычная газировка.
"""


# class Soda():
#     def __init__(self, additive=None):
#         if isinstance(additive, str):
#             self.additive = additive
#         else:
#             self.additive = None
#
#     def show_my_drink(self):
#         if self.additive:
#             print(f"Газировка и {self.additive}")
#         else:
#             print("Обычная газировка")
#
#
# drink1 = Soda()
# drink2 = Soda("Вишня")
# drink3 = Soda(5)
# drink1.show_my_drink()
# drink2.show_my_drink()
# drink3.show_my_drink()


"""
Задача 2

Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. 
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа. 
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.
"""

class TriangleChecker():
    def __init__(self, positive_number):
        if isinstance(positive_number, int):
            self.positive_number = positive_number

        else:
            self.positive_number = None

    def is_triangle(self):
        pass

