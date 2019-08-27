dfa = {'a':{'0':'b', '1':'d'}, 'b':{'0':'a', '1':'c'}, 'c':{'0':'d', '1':'b'}, 'd':{'0':'c', '1':'a'}}
fin = 'a'
str = input('Enter the string: ')
ini = 'a'
nxt = ini
for i in str:
    nxt = dfa[nxt][i]
if nxt==fin:
    print('VALID')
else:
    print('INVALID')