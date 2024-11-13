from model.turing_machine import TuringMachine

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.turingMachineEncrypt import CaesarTuringMachine
from model.turing_machine import TuringMachine


# input format
# k # message
w = "3 # ROMA NO FUE CONSTRUIDA EN UN DIA"

k = int(w[0]) # getting k from w (3)
message = w[4:len(w)] # getting message (ROMA NO FUE CONSTRUIDA EN UN DIA)

print(f"\nw -> {w}\nk -> {k} \nmessage to encrypt -> {message}\n")

#building turing machgine with k 
tm_config = CaesarTuringMachine(k).to_json(filename="config/turing_encrypt_k_"+str(k))

#Creating turing machine from json generated above
tm = TuringMachine(tm_config=tm_config)
tm.display() # displaya turing machine

#loading input (message)
tm.load_input(message)

#Running turing machine
tm.run()

#Showing encrypted message
encrypted_message = tm.get_tape_contents()
print("\nEncrypted message:", encrypted_message)


