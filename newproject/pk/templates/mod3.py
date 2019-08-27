dfa = {'a':{'0':'b', '1':'b'}, 'b':{'0':'c', '1':'c'},'c':{'0':'a', '1':'a'}}
string = input('Enter a string: ')
final = 'a'
ini = 'a'
nxt = ini
for i in string:
    nxt = dfa[nxt][i]
if nxt==final:
    print('VALID')
else:
    print('INVALID')