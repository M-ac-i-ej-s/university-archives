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

# Funkcja do wykonania operacji XOR na dwóch łańcuchach znaków
def xor_strings(string, key):
    text = string.split("\n")
    return ''.join(format(ord(c) ^ ord(k), '08b') for c, k in zip(string, key))

# Funkcja do zaszyfrowania tekstu za pomocą klucza
def encrypt(plaintext, key):
    ciphertext = xor_strings(plaintext, key)
    return ciphertext

# Funkcja do odszyfrowania tekstu za pomocą klucza
def decrypt(ciphertext, key):
    plaintext = xor_strings(ciphertext, key)
    return plaintext

# Funkcja do wykonania kryptoanalizy na podstawie kryptogramu
def cryptanalysis(ciphertext):
    # Nie jest możliwe wykonanie kryptoanalizy w oparciu o sam kryptogram, ponieważ brakuje klucza
    # Program wypisze w tym przypadku komunikat o błędzie
    print("Błąd: Brak klucza do wykonania kryptoanalizy.")
    return

match action:
    case "-p":
        write_file('plain.txt', prepare_text(read_file('orig.txt').replace('\n', ''), 64))
    case "-e":
        write_file('crypto.txt', encrypt(read_file('plain.txt'), read_file('key.txt')))
    case "-k":    
        write_file('decrypt.txt', cryptanalysis(read_file('crypto.txt')))

        
