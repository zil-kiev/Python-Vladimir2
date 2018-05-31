V = int(input('Vvedite chislo:'))


M = V % 60
N = int(V / 60)



while  (N > 23):
    N = int((N - 24))


print('Chasov:', N)
print('Minut:',M)

