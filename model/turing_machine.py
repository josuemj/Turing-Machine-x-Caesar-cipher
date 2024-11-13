import json

class TuringMachine:
    def __init__(self, tm_config):
        """Initializes the Turing Machine by loading dict"""
     

        # Initialize components
        self.Q = set(tm_config["Q"])
        self.Sigma = set(tm_config["Sigma"])
        self.Gamma = set(tm_config["Gamma"])
        self.q0 = tm_config["q0"]
        self.q_accept = tm_config["q_accept"]
        self.q_reject = tm_config.get("q_reject", None)
        self.blank_symbol = tm_config["blank_symbol"]

        # Parse delta function
        self.delta = {}
        for key_str, value_list in tm_config["delta"].items():
            # Convert the key_str back to a tuple (state, symbol)
            # The key_str is like "('q_shift', 'A')"
            key_tuple = eval(key_str)
            new_state, new_symbol, direction = value_list
            self.delta[(key_tuple[0], key_tuple[1])] = (new_state, new_symbol, direction)

        # Initialize the Turing Machine state
        self.current_state = self.q0
        self.tape = []
        self.head_position = 0
        self.configurations = []

    def load_input(self, message):
        """Loads the input message onto the tape."""
        self.tape = list(message.upper()) + [self.blank_symbol]
        self.head_position = 0
        self.current_state = self.q0

    def print_configuration(self):
        """Prints the current configuration of the Turing machine."""
        left = ''.join(self.tape[:self.head_position])
        right = ''.join(self.tape[self.head_position:])
        print(f"Configuration: {left} {self.current_state} {right}")
        self.configurations.append(left + self.current_state + right)

    def step(self):
        """Executes one step of the Turing machine."""
        self.print_configuration()

        # Check if we're in the accepting or rejecting state
        if self.current_state == self.q_accept or self.current_state == self.q_reject:
            return

        # Get the current symbol under the head
        tape_symbol = self.tape[self.head_position]
        action = self.delta.get((self.current_state, tape_symbol))

        if action is None:
            # No defined transition, halt
            if self.q_reject:
                self.current_state = self.q_reject
            else:
                self.current_state = self.q_accept
            return

        new_state, new_symbol, direction = action
        self.tape[self.head_position] = new_symbol
        self.current_state = new_state

        # Move head
        if direction == "R":
            self.head_position += 1
            if self.head_position >= len(self.tape):
                self.tape.append(self.blank_symbol)
        elif direction == "L":
            if self.head_position > 0:
                self.head_position -= 1
            else:
                self.tape.insert(0, self.blank_symbol)
        elif direction == "S":
            pass
        else:
            raise ValueError(f"Invalid direction: {direction}")

    def run(self):
        """Runs the Turing machine until it reaches the accepting or rejecting state."""
        while self.current_state != self.q_accept and self.current_state != self.q_reject:
            self.step()

    def get_tape_contents(self):
        """Returns the contents of the tape after execution."""
        return ''.join(self.tape).rstrip(self.blank_symbol)

    def display(self):
        """Displays the Turing machine's components and transition function."""
        print("\nTuring Machine Components for Caesar Cipher Encryption:")
        print("1. Set of states (Q):", self.Q)
        print("2. Input alphabet (Σ):", self.Sigma)
        print("3. Tape alphabet (Γ):", self.Gamma)
        print("4. Initial state (q0):", self.q0)
        print("5. Accepting state (F):", self.q_accept)
        print("6. Blank symbol (B):", self.blank_symbol)
        print("\nTransition Function (δ):")
        for (state, symbol), (new_state, new_symbol, direction) in self.delta.items():
            print(f"   δ({state}, {symbol}) -> ({new_state}, {new_symbol}, {direction})")
