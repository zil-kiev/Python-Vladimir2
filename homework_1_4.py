name = input('Vvedite imya: ')
line_2 = "*" * 20

len_name = len(name)
line = int(((20-len_name)/2)-2)
line_1 = " " * line

print (line_2)
print('*'+ line_1, name, line_1 + '*')
print (line_2)