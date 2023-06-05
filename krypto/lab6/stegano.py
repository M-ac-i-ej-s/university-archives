# Author: Maciej SŁupianek

import sys
from utils import *

instruction = """
Użycie: python stegano.py [a1] [a2]
a1:
    -e (zanurzenie wiadomości)
    -d (wyodrębnienie wiadomości)
a2:
    -1
    -2
    -3
    -4
"""

if len((sys.argv)) != 3:
    print("Niepoprawna liczba argumentów!")
    print(instruction)
    exit()

if sys.argv[1] not in ["-e", "-d"]:
    print("Niepoprawny argument a1!")
    print(instruction)
    exit()

if sys.argv[2] not in ["-1", "-2", "-3", "-4"]:
    print("Niepoprawny argument a2!")
    print(instruction)
    exit()

if sys.argv[1] == "-e":
    if sys.argv[2] == "-1":
        print("Zanurzenie wiadomości -1 (data/watermark.html)")
        embed_message_method1()
    elif sys.argv[2] == "-2":
        print("Zanurzenie wiadomości -2 (data/watermark.html)")
        embed_message_method2()
    elif sys.argv[2] == "-3":
        print("Zanurzenie wiadomości -3 (data/watermark.html)")
        embed_message_method3()
    elif sys.argv[2] == "-4":
        print("Zanurzenie wiadomości -4 (data/watermark.html)")
        embed_message_method4()
elif sys.argv[1] == "-d":
    if sys.argv[2] == "-1":
        print("Wyodrębnienie wiadomości -1 (data/detect.txt)")
        extract_message_method1()
    elif sys.argv[2] == "-2":
        print("Wyodrębnienie wiadomości -2 (data/detect.txt)")
        extract_message_method2()
    elif sys.argv[2] == "-3":
        print("Wyodrębnienie wiadomości -3 (data/detect.txt)")
        extract_message_method3()
    elif sys.argv[2] == "-4":
        print("Wyodrębnienie wiadomości -4 (data/detect.txt)")
        extract_message_method4()
