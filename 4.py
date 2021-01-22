from collections import namedtuple
from dfa3 import DFA
Transition = namedtuple(
    'transition',
    [
        'cur_state',
        'symbol',
        'next_state',
        'del_of_stack',
        'add_in_stack'
    ]
)
class PDA(DFA):
    def __init__(
        self,
        stack_symbols=[],
        end_of_stack=' ',
        *args,
        **kwargs
    ):
        super().__init__()
        self.stack_symbols=stack_symbols
        self.end_of_stack=end_of_stack
    def add_stack_symbols(self, symbol):
        if symbol not in self.stack_symbols:
            self.stack_symbols.append(symbol)
    def del_stack_symbol(self,symbol):
        if symbol in self.stack_symbols:
            self.stack_symbols.remove(symbol)
    def set_end_stack(self, symbol):
        if symbol in self.stack_symbols:
            self.end_of_stack = symbol
    def init_work(self, buf_string):
        buf_string += '$'
        pda_stack = []
        pda_stack.insert(0, self.end_of_stack)
        cur_state = self.start_state
        for s in buf_string:
            cur_state, del_of_stack, add_in_stack = self.get_next_state(cur_state, s)
            if cur_state == ' ':
                return False
            if del_of_stack != ' ' and (pda_stack or pda_stack[-1] != del_of_stack):
                return False
            if add_in_stack != ' ':
                pda_stack.insert(0,add_in_stack)
        return self.is_end_states(cur_state)

    def get_next_state(self, cur_state, cur_symbol):
        for t in self.transitions:
            if t.cur_state == cur_state and t.symbol == cur_symbol:
                return t.next_state, t.del_of_stack, t.add_in_stack


def init_pda():
    buf_pda = PDA()
    start_state = '1'
    end_states = ['1']
    states = ['1', '2']
    symbols = ['(',')','{','}']
    symbols_stack = ['Δ', 'A', 'B']
    end_of_stack = 'Δ'
    rav_transitions = [
        ['1', '(', '2', ' ', 'A'],
        ['1', '{', '2', ' ', 'B'],
        ['2', '(', '2', ' ', 'A'],
        ['2', '{', '2', ' ', 'B'],
        ['2', ')', '2', 'A', ' '],
        ['2', '}', '2', 'B', ' '],
        ['2', '$', '1', 'Δ', 'Δ']
    ]
    transitions = [
        Transition(*t)
        for t in rav_transitions
    ]
    for state in states:
        buf_pda.add_state(state)
    for s in symbols:
        buf_pda.add_symbol(s)
    for end_state in end_states:
        buf_pda.add_end_state(end_state)
    for t in transitions:
        buf_pda.add_transition(t)
    for s in symbols_stack:
        buf_pda.add_stack_symbols(s)
    buf_pda.set_start_state(start_state)
    buf_pda.set_end_stack(end_states)

    return buf_pda
if __name__ == '__main__':
    pda = init_pda()
    check_automates = [
        "{()(({()}))}",
        "(()){"
    ]
    for ca in check_automates:
        print('Entered line for КАМП', ca)
        print('Result work КАМП')
        if pda.init_work(ca):
            print('line in alphabet')
        else:
            print('line not in alphabet')