from model.turing_machine import TuringMachine
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def process_encryption(key, machineTuring, message):
    """Encrypts the given message using the provided Turing machine configuration."""
    print(f"Encrypting message with key {key}: '{message}'")
    tm_config = machineTuring(key).to_json(filename="config/turing_encrypt_k_" + str(key))
    tm = TuringMachine(tm_config=tm_config)
    tm.display()
    tm.load_input(message)
    tm.run()
    encrypted_message = tm.get_tape_contents()
    print("\nEncrypted message:", encrypted_message)
    return encrypted_message

def process_decryption(key, machineTuring, message):
    """Decrypts the given message using the provided Turing machine configuration."""
    print(f"Decrypting message with key {key}: '{message}'")
    tm_config = machineTuring(key).to_json(filename="config/turing_decrypt_k_" + str(key))
    tm = TuringMachine(tm_config=tm_config)
    tm.display()
    tm.load_input(message)
    tm.run()
    decrypted_message = tm.get_tape_contents()
    print("\nDecrypted message:", decrypted_message)
    return decrypted_message

def handle_request(key, machineTuringEncrypt, machineTuringDecrypt, message, action):
    """Handles encryption or decryption based on the action parameter."""
    if action == "encrypt":
        return process_encryption(key, machineTuringEncrypt, message)
    elif action == "decrypt":
        return process_decryption(key, machineTuringDecrypt, message)
    else:
        raise ValueError("Invalid action. Use 'encrypt' or 'decrypt'.")
