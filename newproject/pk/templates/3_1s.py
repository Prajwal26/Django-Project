dfa = {'a':{'0':'a', '1':'b'},'b':{'0':'a', '1':'c'},'c':{'0':'a', '1':'d'},'d':{'0':'d', '1':'d'}}
string = input('Enter a string: ')
final = 'd'
ini = 'a'
nxt = ini
for i in string:
    nxt = dfa[nxt][i]
if nxt==final:
    print('VALID')
else:
    print('INVALID')