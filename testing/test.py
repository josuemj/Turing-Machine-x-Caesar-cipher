import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.control import handle_request
from model.turingMachineEncrypt import CaesarTuringMachine
from model.turingMachineDecrypt import CaesarDecryptTuringMachine
from main import get_simple_key

# ANSI escape codes for color
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

samples = {
    # message : [k, ecrypted] #expected
    "ROMA NO FUE CONSTRUIDA EN UN DIA": [3, "URPD QR IXH FRQVWUXLGD HQ XQ GLD"],
    # "HOLA MUNDO": [2, "JQNC OWPFQ"],
    "HOLA MUNDO": ["B", "IPMB NVOEP"]
    
}

samples = {
    # message : [k, expected_encrypted_message]
    "ROMA NO FUE CONSTRUIDA EN UN DIA": [3, "URPD QR IXH FRQVWUXLGD HQ XQ GLD"],
    "HOLA MUNDO": ["B", "IPMB NVOEP"],
    "PROGRAMACION": ["E", "TVSKVEQEGMSR"],
    "CIFRADO CESAR": [1, "DJGSBEP DFTBS"],
}

with open('test_result.txt', 'w') as file:
    
    for i in samples:
        print(f'{Colors.HEADER}Message to encrypt (k={samples[i][0]}) -> {i}{Colors.ENDC}')
        key = get_simple_key(str(samples[i][0]))

        # Encryption test
        result = handle_request(
            key,
            CaesarTuringMachine,       # Encryption Turing Machine class
            CaesarDecryptTuringMachine,  # Decryption Turing Machine class
            message=i,                   # Message to process
            action="encrypt"             # Action to perform: "encrypt" or "decrypt"
        )

        print(f'{Colors.OKBLUE}Encrypted message -> {result}{Colors.ENDC}')

        file.write(f"message: {i}\n")
        file.write(f"k = {samples[i][0]}\n")
        file.write(f"result: {result}\n")

        if result == samples[i][1]:
            print(f"{Colors.OKGREEN}ENCRYPTION PASSED{Colors.ENDC}")
            file.write("encryption test result: PASSED\n")
        else:
            print(f"{Colors.FAIL}ENCRYPTION FAILED{Colors.ENDC}")
            file.write("encryption test result: FAILED\n")


        # Decryption test
        result_decrypt = handle_request(
            key,
            CaesarTuringMachine,       # Encryption Turing Machine class
            CaesarDecryptTuringMachine,  # Decryption Turing Machine class
            message=result,             # Message to process
            action="decrypt"            # Action to perform: "encrypt" or "decrypt"
        )
        
        file.write(f"message to rdecrypt: {result}\n")
        file.write(f"decrypted message: {result_decrypt}\n")

        print(f'{Colors.HEADER}Message to decrypt (k={samples[i][0]}) -> {result}{Colors.ENDC}')
        print(f'{Colors.OKCYAN}Decrypted message -> {result_decrypt}{Colors.ENDC}')

        if result_decrypt == i:
            print(f"{Colors.OKGREEN}DECRYPTION PASSED{Colors.ENDC}")
            file.write("decryption test result: PASSED\n \n")

        else:
            print(f"{Colors.FAIL}DECRYPTION FAILED{Colors.ENDC}")
            file.write("decryption test result: FAILED\n \n")
    
        
