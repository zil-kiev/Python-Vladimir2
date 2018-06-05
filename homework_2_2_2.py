a = int (input('введите число а:'))
b = int (input('введите число b:'))
c = int (input('введите число с:'))

if   a == b or a == c or b == c:
        print('a увеличиваем на 5', a+5 ==a)
        print('b увеличиваем на 5', b == b + 5)
        print('c увеличиваем на 5', c == c + 5)
else:
        print('равных нет')