a = input('a: ')
b = input('b: ')
c = input('c: ')

#m = a
#if m < b:
 #   m = b
#if m < c:
 #   m = c



#m_m = len(m)


#print (m_m * '*')
#print('*'+ a + '*')
#print (m_m * '*')
a1 = len(a)
b1 = len(b)
c1 = len(c)

if ((a1 > b1) & (a1 > c1)):
    m = a1 + 2
elif ((b1 > a1) & (b1 > c1)):
    m = b1 + 2
else:
    m = c1 + 2




print(m * "*");

print('*',a + m*'*')
print('*',b)
print('*',c);
print(m * "*");



