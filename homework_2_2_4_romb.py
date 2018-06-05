s = int(input('введите значение: '))
if s%2 == 1:
        for i in range(1,s,2):
            i = ' ' * ((s-i)//2)  + '*' *i + ' ' * (s-i)
            print(i)
        for i in range(s,0,-2):
            i = ' ' * ((s-i)//2)  + '*' *i + ' ' * (s-i)
            print(i)