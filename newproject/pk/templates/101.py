machine = {'a':{'0':'a', '1':'b'},'b':{'0':'c', '1':'a'},'c':{'0':'a', '1':'d'},'d':{'0':'a', '1':'b'}}
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