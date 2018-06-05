import math
Skr = float(input('введите площадь круга:'))
Skv = float(input('введите площать квадрата:'))

stor = Skv ** 0.5
diag = stor * 2 ** 0.5

diam = 2 * (Skr / math.pi ** 0.5)


if diam <= stor:
    print('Круг впишется в квадрат')
else:
    print('Круг не впишется в квадрат')
if diag <= diam:
    print('Квадрат впишется в круг')
else:
    print('Квадрат не впишется в круг')




