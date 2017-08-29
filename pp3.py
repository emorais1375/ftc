import logging
from itertools import islice


class TuringMachine:

    def __init__(self, transitions, start_state='q0', accept_state='qa', reject_state='qr', blank_symbol=''):
        self.blank_symbol = blank_symbol
        self.transitions = transitions
        self.start_state = start_state
        self.reject_state = reject_state

        self.states_to_actions = {
            accept_state: 'Accept',
            reject_state: 'Reject',
        }

    def run(self, input_):
        state = self.start_state

        left_hand_side = [self.blank_symbol]
        if not input_:
            input_ = [self.blank_symbol]

        symbol = input_[0]
        right_hand_side = list(input_[1:])

        while True:
            action = self.states_to_actions.get(state)
            yield (
                action,
                {
                    'state': state,
                    'left_hand_side': left_hand_side,
                    'symbol': symbol,
                    'right_hand_side': right_hand_side,
                }
            )

            if action is not None:
                break

            state, symbol, direction = self.transitions.get(
                (state, symbol),
                (self.reject_state, symbol, 'R'),
            )

            # print(state, symbol, direction)

            if direction == 'R':
                left_hand_side.insert(0, symbol)

                try:
                    symbol = right_hand_side.pop(0)
                except IndexError:
                    symbol = self.blank_symbol

            elif left_hand_side:
                right_hand_side.insert(0, symbol)
                symbol = left_hand_side.pop(0)

    def accepts(self, input_, step_limit=1000000000000000000):
        action = list(islice(self.run(input_), step_limit))[-1][0]

        if action is not None:
            return action == 'Accept'
        else:
            logging.warn(
                'The step limit of %s steps  is reached!',
                step_limit,
            )


transition_function = {
    ("q0", ""): ("q12", "", "L"),

    ("q12", "X"): ("q12", "X", "L"),
    ("q12", ""): ("q13", "", "R"),

    ("q0", "b"): ("q0", "b", "R"),
    ("q0", "c"): ("q0", "c", "R"),
    ("q0", "d"): ("q0", "d", "R"),
    ("q0", "e"): ("q0", "e", "R"),
    ("q0", "f"): ("q0", "f", "R"),
    ("q0", "X"): ("q0", "X", "R"),
    ("q0", "a"): ("q1", "X", "L"),

    ("q1", "a"): ("q1", "a", "L"),
    ("q1", "b"): ("q1", "b", "L"),
    ("q1", "c"): ("q1", "c", "L"),
    ("q1", "d"): ("q1", "d", "L"),
    ("q1", "e"): ("q1", "e", "L"),
    ("q1", "f"): ("q1", "f", "L"),
    ("q1", "X"): ("q1", "X", "L"),
    ("q1", ""): ("q2", "", "R"),

    ("q2", "a"): ("q2", "a", "R"),
    ("q2", "c"): ("q2", "c", "R"),
    ("q2", "d"): ("q2", "d", "R"),
    ("q2", "e"): ("q2", "e", "R"),
    ("q2", "f"): ("q2", "f", "R"),
    ("q2", "X"): ("q2", "X", "R"),
    ("q2", "b"): ("q3", "X", "L"),

    ("q3", "a"): ("q3", "a", "L"),
    ("q3", "b"): ("q3", "b", "L"),
    ("q3", "c"): ("q3", "c", "L"),
    ("q3", "d"): ("q3", "d", "L"),
    ("q3", "e"): ("q3", "e", "L"),
    ("q3", "f"): ("q3", "f", "L"),
    ("q3", "X"): ("q3", "X", "L"),
    ("q3", ""): ("q4", "", "R"),

    ("q4", "a"): ("q4", "a", "R"),
    ("q4", "b"): ("q4", "b", "R"),
    ("q4", "d"): ("q4", "d", "R"),
    ("q4", "e"): ("q4", "e", "R"),
    ("q4", "f"): ("q4", "f", "R"),
    ("q4", "X"): ("q4", "X", "R"),
    ("q4", "c"): ("q5", "X", "L"),

    ("q5", "a"): ("q5", "a", "L"),
    ("q5", "b"): ("q5", "b", "L"),
    ("q5", "c"): ("q5", "c", "L"),
    ("q5", "d"): ("q5", "d", "L"),
    ("q5", "e"): ("q5", "e", "L"),
    ("q5", "f"): ("q5", "f", "L"),
    ("q5", "X"): ("q5", "X", "L"),
    ("q5", ""): ("q6", "", "R"),

    ("q6", "a"): ("q6", "a", "R"),
    ("q6", "b"): ("q6", "b", "R"),
    ("q6", "c"): ("q6", "c", "R"),
    ("q6", "e"): ("q6", "e", "R"),
    ("q6", "f"): ("q6", "f", "R"),
    ("q6", "X"): ("q6", "X", "R"),
    ("q6", "d"): ("q7", "X", "L"),

    ("q7", "a"): ("q7", "a", "L"),
    ("q7", "b"): ("q7", "b", "L"),
    ("q7", "c"): ("q7", "c", "L"),
    ("q7", "d"): ("q7", "d", "L"),
    ("q7", "e"): ("q7", "e", "L"),
    ("q7", "f"): ("q7", "f", "L"),
    ("q7", "X"): ("q7", "X", "L"),
    ("q7", ""): ("q8", "", "R"),

    ("q8", "a"): ("q8", "a", "R"),
    ("q8", "b"): ("q8", "b", "R"),
    ("q8", "c"): ("q8", "c", "R"),
    ("q8", "d"): ("q8", "d", "R"),
    ("q8", "f"): ("q8", "f", "R"),
    ("q8", "X"): ("q8", "X", "R"),
    ("q8", "e"): ("q9", "X", "L"),

    ("q9", "a"): ("q9", "a", "L"),
    ("q9", "b"): ("q9", "b", "L"),
    ("q9", "c"): ("q9", "c", "L"),
    ("q9", "d"): ("q9", "d", "L"),
    ("q9", "e"): ("q9", "e", "L"),
    ("q9", "f"): ("q9", "f", "L"),
    ("q9", "X"): ("q9", "X", "L"),
    ("q9", ""): ("q10", "", "R"),

    ("q10", "a"): ("q10", "a", "R"),
    ("q10", "b"): ("q10", "b", "R"),
    ("q10", "c"): ("q10", "c", "R"),
    ("q10", "e"): ("q10", "e", "R"),
    ("q10", "d"): ("q10", "d", "R"),
    ("q10", "X"): ("q10", "X", "R"),
    ("q10", "f"): ("q11", "X", "L"),

    ("q11", "a"): ("q11", "a", "L"),
    ("q11", "b"): ("q11", "b", "L"),
    ("q11", "c"): ("q11", "c", "L"),
    ("q11", "d"): ("q11", "d", "L"),
    ("q11", "e"): ("q11", "e", "L"),
    ("q11", "f"): ("q11", "f", "L"),
    ("q11", "X"): ("q11", "X", "L"),
    ("q11", ""): ("q0", "", "R")

}

one_hash = TuringMachine(transition_function, start_state='q0', accept_state='q13', reject_state='qr', blank_symbol="")


try:
    string = input()
    if one_hash.accepts(string):
        print(string, "ACEITA")
    else:
        print(string, "REJEITA")
except:
    print(" ACEITA")
