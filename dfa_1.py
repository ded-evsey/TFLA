Transition = namedtuple(
    'Transition',
    'current_state symbol next_state'
)
class DFA:
    def __init__(self, states=[], symbols=[], start_state='', end_states=[], transitions=[]):
        self.states = states
        self.symbols = symbols
        self.start_state = start_state
        self.end_states = end_states
        self.transitions = transitions
    def add_state(self, state):
        if state not in self.states:
            self.states.append(state)

    def del_state(self, state):
        if state in self.states:
            self.states.remove(state)

    def add_symbol(self, symbol):
        if symbol not in self.symbols:
            self.symbols.append(symbol)

    def del_symbol(self, symbol):
        if symbol in self.symbols:
            self.symbols.remove(symbol)

    def set_start_state(self, start_state):
        if start_state in self.states:
            self.start_state = start_state

    def add_end_state(self, end_state):
        if end_state in self.states:
            self.end_states.append(end_state)

    def del_end_state(self, end_state):
        if end_state in self.states and end_state in self.end_states:
            self.end_states.remove(end_state)

    def add_transition(self, _transition):
        if _transition not in self.transitions:
            self.transitions.append(_transition)


    def get_next_state(self, cur_state, cur_symbol):
        for t in self.transitions:
            if t.current_state == cur_state and t.symbol == cur_symbol:
                return t.next_state
        return ' '

    def is_end_states(self, cur_state):
        return cur_state in self.end_states

    def init_work(self, buf_string):
        cur_state = self.start_state
        for s in buf_string:
            cur_state = self.get_next_state(cur_state, s)
            if cur_state == " ":
                return False
        return self.is_end_states(cur_state)