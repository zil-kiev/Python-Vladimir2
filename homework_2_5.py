a = int (input('введите число а:'))
b = int (input('введите число b:'))

if   10 <= a <= 99:


     if a // 10 == b or  a % 10 == b:
        print('входит b')
     else:
        print('не входит b')
else:
    print('введите корректное число a ')