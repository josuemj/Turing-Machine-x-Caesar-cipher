from model.turing_machine import TuringMachine

import sys
import os
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.turingMachineEncrypt import CaesarTuringMachine
from model.turingMachineDecrypt import CaesarDecryptTuringMachine
from controller.control import handle_request


def get_action():
    """Prompt the user for the action and validate input."""
    while True:
        action = input("Enter action (encrypt/decrypt): ").strip().lower()
        if action in {"encrypt", "decrypt"}:
            return action
        else:
            print("Invalid action. Please enter 'encrypt' or 'decrypt'.\n")

def get_key():
    """Prompt the user for the shift key as a positive integer or a letter."""
    while True:
        key_input = input("Enter the Caesar cipher shift key (positive integer or letter): ").strip()
        
        if key_input.isdigit():
            # If input is a digit, ensure it's a positive integer
            k = int(key_input)
            if k > 0:
                return k
            else:
                print("Key must be a positive integer.\n")
        
        elif re.match("^[A-Za-z]$", key_input):
            # If input is a single letter, calculate its position in the alphabet
            key_letter = key_input.upper()
            k = ord(key_letter) - ord('A')  # Position in alphabet minus 1
            return k
        
        else:
            print("Invalid input. Please enter a positive integer or a single letter.\n")


def get_message():
    """Prompt the user for the message and ensure it contains only letters and spaces."""
    while True:
        message = input("Enter the message (letters and spaces only): ").strip().upper()
        if re.match("^[A-Z ]+$", message):
            return message
        else:
            print("Invalid message. Please use letters and spaces only, no numbers or special characters.\n")

# Main script
if __name__ == "__main__":
    # Get user inputs
    action = get_action()
    k = get_key()
    message = get_message()

    # Call handle_request with appropriate Turing machine classes
    print("\n")
    result = handle_request(
        k,
        CaesarTuringMachine,       # Encryption Turing Machine class
        CaesarDecryptTuringMachine, # Decryption Turing Machine class
        message,                   # Message to process
        action                      # Action to perform: "encrypt" or "decrypt"
    )
