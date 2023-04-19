# autorem programu jest: Maciej Słupianek
import sys
import math

typeCrypt = sys.argv[1]
typeAction = sys.argv[2]

if(typeCrypt != "-c" and typeCrypt != "-a"):
    print("Wrong type of crypt")
    exit()

if(typeAction != "-e" and typeAction != "-d" and typeAction != "-j" and typeAction != "-k"):
    print("Wrong type of action")
    exit()

# take text from file
def take_text_from_file(file_name):
    file = open(file_name, "r")
    text = file.read()
    file.close()
    return text

def safe_to_file(file_name, text):
    open(file_name, "x")
    with open(file_name, 'w') as the_file:
        the_file.write(text)

def encrypt_text_c(plaintext,n):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch == " ":
            ans += " "
        elif (ch.isupper()):
            ans += chr((ord(ch) + int(n) - 65) % 26 + 65)
        else:
            ans += chr((ord(ch) + int(n) - 97) % 26 + 97)
    return ans

def decrypt_text_c(encrypted_message, k):
    letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_message = ""

    for ch in encrypted_message:
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - int(k)) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch
    return decrypted_message

def find_number_of_encryption_c(decrypted_message,encrypted_message):
    number_of_encryption = 1
    for i in range(1, 26):
        print(decrypt_text_c(decrypted_message, i))
        if encrypted_message.lower() in decrypt_text_c(decrypted_message, i):
            number_of_encryption = i
    return number_of_encryption

def find_uncrypted_text_c(encrypted_message):
    arrOfResults = []
    for i in range(1, 26):
        arrOfResults.append(decrypt_text_c(encrypted_message, i))
    return arrOfResults   

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# function to encrypt a single letter
def encrypt_letter(p, a, b):
    return (a * p + b) % 26

# function to decrypt a single letter
def decrypt_letter(c, a, b):
    a_inv = mod_inverse(a, 26)
    return (a_inv * (c - b)) % 26

# function to encrypt a string
def encrypt_text_a(plaintext, a, b):
    ciphertext = ''
    for p in plaintext:
        if p.isalpha():
            # convert letter to number (A=0, B=1, etc.)
            p_num = ord(p.upper()) - 65
            c_num = encrypt_letter(p_num, a, b)
            # convert number back to letter
            c = chr(c_num + 65)
        else:
            # non-alphabetic characters are unchanged
            c = p
        ciphertext += c
    return ciphertext

# function to decrypt a string
def decrypt_text_a(ciphertext, a, b):
    plaintext = ''
    for c in ciphertext:
        if c.isalpha():
            # convert letter to number (A=0, B=1, etc.)
            c_num = ord(c.upper()) - 65
            p_num = decrypt_letter(c_num, a, b)
            # convert number back to letter
            p = chr(p_num + 65)
        else:
            # non-alphabetic characters are unchanged
            p = c
        plaintext += p
    return plaintext

def find_number_of_encryption_a(encrypted_message, decrypted_message):
    number_of_encryption = []
    for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
        for k in range(1, 26):
            if decrypted_message.upper() in decrypt_text_a(encrypted_message, i,k):
                print(i,k)
                number_of_encryption = [i,k]
                break
        if number_of_encryption != []:
            break    
    return number_of_encryption

def find_uncrypted_text_a(encrypted_message):
    number_of_encryptions = []
    for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
        for k in range(1, 27):
                number_of_encryptions.append(decrypt_text_a(encrypted_message, i,k)) 
    return number_of_encryptions

text_from_plain = take_text_from_file("plain.txt")
text_from_key = take_text_from_file("key.txt")
text_from_extra = take_text_from_file("extra.txt")

parameters = [int(text_from_key[0]), int(text_from_key[2])]


match typeCrypt:
    case "-c":
        match typeAction:
            case "-e":
                # crypt cesar code
                safe_to_file("crypto.txt", "\n" + encrypt_text_c(text_from_plain, parameters[0]))
            case "-d":
                # decrypt cesar code
                safe_to_file("decrypt.txt",  "\n" +  decrypt_text_c(text_from_plain, parameters[0]))
            case "-j":
                # crypt cesar code with key
                text_from_crypto = take_text_from_file("crypto.txt")
                safe_to_file("key-found.txt",  "\n" + str(find_number_of_encryption_c(text_from_crypto,text_from_extra)))
            case "-k":            
                # cryptoanalysis cesar code
                text_from_crypto = take_text_from_file("crypto.txt")
                arr = find_uncrypted_text_c(text_from_crypto)
                someStr = "\ndecrypted text:\n"
                for i in range(len(arr)):
                    someStr += "key" + str(i) + ": " + arr[i] + "\n"
                safe_to_file("crypto.txt", someStr)
    case "-a":    
        match typeAction:
            case "-e":
                safe_to_file("crypto.txt",  "\n" + encrypt_text_a(text_from_plain, parameters[0], parameters[1]))
            case "-d":
                safe_to_file("decrypt.txt",  "\n" +  decrypt_text_a(text_from_extra, parameters[0], parameters[1]))
            case "-j":
                text_from_crypto = take_text_from_file("crypto.txt")
                safe_to_file("key-found.txt",  "\n" + str(find_number_of_encryption_a(text_from_crypto,text_from_extra)))
            case "-k": 
                text_from_crypto = take_text_from_file("crypto.txt")
                arr = find_uncrypted_text_a(text_from_crypto)
                someStr = "\ndecrypted text:\n"
                for i in range(len(arr)):
                    someStr += "\n" + "key" + str(i) + ": " + arr[i] 
                safe_to_file("crypto.txt", someStr)
    case _ : 
        print('coś poszło nie tak')            

