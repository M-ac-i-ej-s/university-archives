#autor: Maciej Słupianek
import argparse
import sys

action = sys.argv[1]

if(action != "-p" and action != "-e" and action != "-k"):
    print("Wrong type of crypt")
    exit()

# Funkcja do odczytu pliku i zwrócenia jego zawartości w postaci łańcucha znaków
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Funkcja do zapisu łańcucha znaków do pliku
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# Funkcja do przygotowania tekstu do działania (dodaje padding i dzieli na linijki)
def prepare_text(text, line_length):
    padded_text = text.ljust(len(text) + (line_length - (len(text) % line_length)))
    return '\n'.join([padded_text[i:i+line_length] for i in range(0, len(padded_text), line_length)])

def text_to_binary(text):
    binary = ""
    for char in text:
        binary += format(ord(char), "08b")
    return binary

def encrypt(text, key):
    text = text.lower()
    text = text.split("\n")
    crypto = []
    for line in text:
        crypto_line = ""
        for index, char in enumerate(line):
            crypto_line += format(int(text_to_binary(char), 2) ^ int(text_to_binary(key[index]), 2), "08b")
        crypto.append(crypto_line)
    f = open("crypto.txt", "w")
    for index, line in enumerate(crypto):
        if index == 0:
            f.write(line)
        else:
            f.write("\n" + line)
    f.close()

def binary_to_text(binary):
    text = ""
    for i in range(0, len(binary), 8):
        text += chr(int(binary[i:i+8], 2))
    return text

# Funkcja do odszyfrowania tekstu za pomocą klucza
def cryptanalysis(line_length, crypto):
    key = ["#" for i in range(line_length)]
    crypto1 = crypto.split("\n")
    if crypto1[-1] == "":
        crypto1 = crypto1[:-1]

    for i in range(len(crypto1)):
        for j in range(0, len(crypto1[i]), 8):
            if crypto1[i][j] == "0" and crypto1[i][j+1] == "1" and crypto1[i][j+2] == "0":
                key[j//8] = chr(int(crypto1[i][j:j+8], 2) ^ 32)
    key = "".join(key)
    print("key: " + key)
    return decrypt(key, line_length, crypto)

def decrypt(key, line_length, crypto):
    crypto = crypto.split("\n")

    decrypt = []
    for line in crypto:
            decrypt_line = ""
            j = 0
            for i in range(0, len(line), 8):
                if key[j] == "#":
                    decrypt_line += format(int(text_to_binary("#"), 2), "08b")
                else:
                    decrypt_line += format(int(text_to_binary(key[j]),
                                               2) ^ int(line[i:i+8], 2), "08b")
                j += 1
            decrypt.append(binary_to_text(decrypt_line))

    return "".join(decrypt)

match action:
    case "-p":
        write_file('plain.txt', prepare_text(read_file('orig.txt').replace('\n', ''), 64))
    case "-e":
        encrypt(read_file('plain.txt'), read_file('key.txt'))
    case "-k":    
        write_file('decrypt.txt', cryptanalysis(64,read_file('crypto.txt')))

        
