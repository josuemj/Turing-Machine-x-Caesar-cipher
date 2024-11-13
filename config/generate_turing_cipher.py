import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.turingMachineEncrypt import CaesarTuringMachine

#generate turing machine and write JSON

k=3
tm = CaesarTuringMachine(k).to_json(filename="config/turing_encrypt_k_"+str(k))
