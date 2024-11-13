from model.turing_machine import TuringMachine

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.turingMachineEncrypt import CaesarTuringMachine
from model.turingMachineDecrypt import CaesarDecryptTuringMachine
from controller.control import handle_request
from model.turing_machine import TuringMachine


# input format: <mode> <k> # <message>
# Example for encryption: "encrypt 3 # ROMA NO FUE CONSTRUIDA EN UN DIA"
# Example for decryption: "decrypt 3 # URPD QR IXH FRQVWUXLFD HQ XQ GLD"
w = "decrypt 3 # URPD QR IXH FRQVWUXLGD HQ XQ GLD"
action, k, message = w.split(" ", 2)  # Split mode, k, and message
k = int(k)
message = message[2:]  # Remove the '# ' separator

# Call handle_request with appropriate Turing machine classes
result = handle_request(
     k,
     CaesarTuringMachine,       # Encryption Turing Machine class
     CaesarDecryptTuringMachine, # Decryption Turing Machine class
    message,                   # Message to process
    action                      # Action to perform: "encrypt" or "decrypt"
)