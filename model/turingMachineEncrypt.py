import json
import string

class CaesarTuringMachine:
    def __init__(self, k):
        # Define components based on Caesar cipher shift
        self.Q = {"q0", "q_shift", "q_done"}
        self.Sigma = set(string.ascii_uppercase) | {" "}
        self.Gamma = set(string.ascii_uppercase) | {" ", "B"}
        self.q0 = "q0"
        self.q_done = "q_done"
        self.blank_symbol = "B"
        
        # Generate delta (transition function) dynamically for shift k
        self.delta = self.generate_delta(k)
        
        # Initialize other configurations
        self.current_state = self.q0
        self.tape = []
        self.head_position = 0
        self.configurations = []

    def generate_delta(self, k):
        """Generates the transition function for Caesar cipher with shift k."""
        delta = {}

        # Transition from 'q0' to 'q_shift' without changing the tape
        delta[("q0", "B")] = ("q_shift", "B", "S")

        # Create transitions to shift each letter by k positions
        for letter in string.ascii_uppercase:
            shifted_letter = self.shift_letter(letter, k)
            delta[("q_shift", letter)] = ("q_shift", shifted_letter, "R")
        
        # Handle spaces: they should remain unchanged
        delta[("q_shift", " ")] = ("q_shift", " ", "R")
        
        # Transition to stop when hitting blank
        delta[("q_shift", "B")] = ("q_done", "B", "S")
        
        return delta


    def shift_letter(self, letter, k):
        """Shifts a letter by k positions in the alphabet."""
        alphabet = string.ascii_uppercase
        index = alphabet.index(letter)
        new_index = (index + k) % len(alphabet)
        return alphabet[new_index]

    def load_input(self, message):
        """Loads the input message onto the tape."""
        self.tape = list(message.upper()) + ["B"]  # Convert message to uppercase
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

        # Check if we're in the accepting state
        if self.current_state == self.q_done:
            return

        # Get the current symbol under the head
        tape_symbol = self.tape[self.head_position]
        action = self.delta.get((self.current_state, tape_symbol))

        if action is None:
            # No defined transition, halt
            self.current_state = self.q_done
            return

        new_state, new_symbol, direction = action
        self.tape[self.head_position] = new_symbol
        self.current_state = new_state

        # Move head
        if direction == "R":
            self.head_position += 1
            if self.head_position >= len(self.tape):
                self.tape.append("B")

    def run(self):
        """Runs the Turing machine until it reaches the q_done state."""
        # Move to q_shift to start processing
        self.current_state = "q_shift"
        
        while self.current_state != self.q_done:
            self.step()

    def get_tape_contents(self):
        """Returns the encrypted contents of the tape."""
        return ''.join(self.tape).rstrip("B")

    def display(self):
        """Displays the Turing machine's components and transition function."""
        print("\nTuring Machine Components for Caesar Cipher Encryption:")
        print("1. Set of states (Q):", self.Q)
        print("2. Input alphabet (Σ):", self.Sigma)
        print("3. Tape alphabet (Γ):", self.Gamma)
        print("4. Initial state (q0):", self.q0)
        print("5. Accepting state (F):", self.q_done)
        print("6. Blank symbol (B):", self.blank_symbol)
        print("\nTransition Function (δ):")
        for (state, symbol), (new_state, new_symbol, direction) in self.delta.items():
            print(f"   δ({state}, {symbol}) -> ({new_state}, {new_symbol}, {direction})")
        
    def to_json(self, filename=None):
        """Returns the Turing machine's configuration as a dictionary. Optionally saves it to a JSON file."""
        turing_machine_dict = {
            "Q": list(self.Q),
            "Sigma": list(self.Sigma),
            "Gamma": list(self.Gamma),
            "delta": {str(key): list(value) for key, value in self.delta.items()},
            "q0": "q_shift",  # Set initial state to 'q_shift'
            "q_accept": self.q_done,
            "q_reject": None,
            "blank_symbol": self.blank_symbol
        }
        
        if filename:
            # Write the dictionary to a JSON file
            with open(filename, 'w') as json_file:
                json.dump(turing_machine_dict, json_file, indent=2)
            print(f"Turing Machine configuration saved to {filename}")
        
        return turing_machine_dict


        

# Usage example
if __name__ == "__main__":
    k = 3  # Example shift for Caesar cipher
    message = "ROMA NO FUE CONSTRUIDA EN UN DIA"
    
    caesar_tm = CaesarTuringMachine(k)
    caesar_tm.display()
    caesar_tm.load_input(message)
    caesar_tm.run()
    print("\nEncrypted Tape Contents:", caesar_tm.get_tape_contents())
