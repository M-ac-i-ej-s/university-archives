# Author: Szymon Kalkowski

import sys
from utils import *

instruction = """
Użycie: python xor.py [a1]
a1:
    -p (przygotowanie tekstu do przykładu działania)
    -e (szyfrowanie)
    -k (kryptoanaliza wyłącznie w oparciu o kryptogram)

"""

if len((sys.argv)) != 2:
    print("Niepoprawna liczba argumentów!")
    print(instruction)
    exit()

if sys.argv[1] not in ["-p", "-e", "-k"]:
    print("Niepoprawny argument a1!")
    print(instruction)
    exit()

if sys.argv[1] == "-p":
    print("Przygotowanie tekstu do przykładu działania (data/plain.txt)")
    prepare_text()
elif sys.argv[1] == "-e":
    print("Szyfrowanie (data/crypto.txt)")
    encryption()
elif sys.argv[1] == "-k":
    print("Kryptoanaliza wyłącznie w oparciu o kryptogram (data/decrypt.txt)")
    cryptanalysis()
