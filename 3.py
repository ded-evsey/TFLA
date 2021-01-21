from dfa1 import DFA, Transition


def init_dfa():
    buf_dfa = DFA()
    start_state = '0'
    end_states = ['2']
    states = ['0','1','2']
    eng_symbols = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num_symbols = ['1', '2', '3', '4', '5','6', '7', '8', '9', '0']

    cur_transitions = []
    for s in eng_symbols:
        cur_transitions.append(
            Transition('0',s,'1')
        )
        buf_dfa.add_symbol(s)

    for n in num_symbols:
        cur_transitions.append(
            Transition('1',n,'2')
        )
        cur_transitions.append(
            '2',n,'2'
        )
        buf_dfa.add_symbol(n)
    for state in  states:
        buf_dfa.add_state(state)
    buf_dfa.set_start_state(start_state)
    for state in end_states:
        buf_dfa.add_end_state(state)
    for t in cur_transitions:
        buf_dfa.add_transition(t)
    return buf_dfa
if __name__ == '__main__':
    one_dfa = init_dfa()
    check_automate_lines = 'a1234591'
    for check_automate in check_automate_lines:
        print('Entered line for  DFA', check_automate)
        print('Result work DFA')
        if one_dfa.init_work(check_automate):
            print('line in alphabet')
        else:
            print('line not in alphabet')