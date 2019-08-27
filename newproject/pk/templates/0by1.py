dfa= {'a':{'0':'b', '1':'a'}, 'b':{'0':'b', '1':'c'}, 'c':{'0':'c', '1':'c'}}
final = 'c'
string = input('Enter the string: ')
initial = 'a'
nxt = initial
for i in string:
    nxt = dfa[nxt][i]
if nxt ==final:
    print('VALID')
else:
    print('INVALID')