#for i in range(1,5):


 #   for a in range(1,5):
  #      print(i * '{}\n'.format(a * '*'))

       # print('*', end='\n')
        # print('*', end='')

s = input()
    line = s
    i = '*'
    j = ' '
    if s%2 == 1:
        for i in range(s):
            i = ' ' * (1 + s) * 2 + '*' * (line + s/2) * 2 + ' ' * (1 + s)
            print i
    else:
        print "you're star"