class DFA:
    def __init__(self, num_states, final, initial=0):
        self.machine = [{} for i in range(num_states)]
        self.final = final
        self.initial = 0

    def moves(self, strt, char, end):
        self.machine[strt][char] = end

    def accept(self, string):
        self.string = string
        nxt = self.initial
        for i in string:
            nxt = self.machine[nxt][i]
        if nxt is self.final:
            return 'Valid'
        else:
            return 'Invalid'
state = int(input('Enter total states: '))
ip_chars = int(input('Enter total input characters: '))
ini = int(input('Enter initial state: '))
fin = int(input('Enter final state: '))
dfa = DFA(state, fin, ini)
for i in range(state*ip_chars):
    strt = int(input('Enter start state: '))
    ip = input('Enter input character: ')
    end = int(input('Enter target state: '))
    dfa.moves(strt, ip, end)
ip_str = input("Enter String to be checked: ")
print(dfa.accept(ip_str))
