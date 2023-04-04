import random


line_length = 64


def key_generator():
    key = ""
    for i in range(line_length):
        key += chr(random.randint(97, 122))
    return key


def text_to_binary(text):
    binary = ""
    for char in text:
        binary += format(ord(char), "08b")
    return binary


def binary_to_text(binary):
    text = ""
    for i in range(0, len(binary), 8):
        text += chr(int(binary[i:i+8], 2))
    return text


def decrypt(key):
    f = open("data/crypto.txt", "r")
    crypto = f.read()
    f.close()

    crypto = crypto.split("\n")
    if crypto[-1] == "":
        crypto = crypto[:-1]

    decrypt = []
    for line in crypto:
        if len(line) != line_length * 8:
            print("Niepoprawny kryptogram do odszyfrowania!")
            print(line)
            print(len(line))
            exit()
        else:
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

    f = open("data/decrypt.txt", "w")
    for index, line in enumerate(decrypt):
        if index == 0:
            f.write(line)
        else:
            f.write("\n" + line)
    f.close()


def prepare_text():
    f = open("data/orig.txt", "r")
    text = f.read()
    clear_text = ""
    for char in text:
        if char.isalpha():
            clear_text += char.lower()
        elif char == "\n" or char == " ":
            clear_text += " "

    formated_text = ""
    for i in range(0, len(clear_text), line_length):
        formated_text += clear_text[i:i+line_length] + "\n"

    lines = formated_text.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]

    if len(lines[-1]) < line_length:
        lines[-1] = lines[-1] + "a" * (line_length - len(lines[-1]))
    formated_text = "\n".join(lines)

    f.close()
    f = open("data/plain.txt", "w")
    f.write(formated_text)
    f.close()


def encryption():
    f = open("data/key.txt", "r")
    key = f.read()
    f.close()
    if len(key) != line_length:
        print("Niepoprawny klucz! Generowanie nowego klucza (data/key.txt)")
        f = open("data/key.txt", "w")
        key = key_generator()
        f.write(key)
        f.close()
    f = open("data/plain.txt", "r")
    text = f.read()
    f.close()
    text = text.split("\n")
    crypto = []
    for line in text:
        if len(line) != line_length:
            print("Niepoprawny tekst do szyfrowania!")
            print(line)
            print(len(line))
            exit()
        else:
            crypto_line = ""
            for index, char in enumerate(line):
                crypto_line += format(int(text_to_binary(char),
                                          2) ^ int(text_to_binary(key[index]), 2), "08b")
            crypto.append(crypto_line)
    f = open("data/crypto.txt", "w")
    for index, line in enumerate(crypto):
        if index == 0:
            f.write(line)
        else:
            f.write("\n" + line)
    f.close()


def cryptanalysis():
    key = ["#" for i in range(line_length)]

    f = open("data/crypto.txt", "r")
    crypto = f.read()
    f.close()

    crypto = crypto.split("\n")
    if crypto[-1] == "":
        crypto = crypto[:-1]

    for i in range(len(crypto)):
        for j in range(0, len(crypto[i]), 8):
            if crypto[i][j] == "0" and crypto[i][j+1] == "1" and crypto[i][j+2] == "0":
                key[j//8] = chr(int(crypto[i][j:j+8], 2) ^ 32)
    key = "".join(key)
    print("Znaleziony klucz: " + key)

    f = open("data/key.txt", "w")
    f.write(key)
    f.close()

    decrypt(key)
