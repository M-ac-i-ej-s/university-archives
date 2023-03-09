# autorem programu jest: Maciej Słupianek
import sys

typeCrypt = sys.argv[1]
typeAction = sys.argv[2]

if(typeCrypt != "-c" or typeCrypt != "-a"):
    print("Wrong type of crypt")
    exit()

if(typeAction != "-e" or typeAction != "-d" or typeAction != "-j" or typeAction != "-k"):
    print("Wrong type of action")
    exit()

# take text from file
def take_text_from_file(file_name):
    file = open(file_name, "r")
    text = file.read()
    file.close()
    return text

def safe_to_file(file_name, text):
    with open(file_name, 'a') as the_file:
        the_file.write(text)

def encrypt_text_c(plaintext,n):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    return ans

def decrypt_text_c(encrypted_message, k):
    letters="abcdefghijklmnopqrstuvwxyz"
    decrypted_message = ""

    for ch in encrypted_message:
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - k) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch
    return decrypted_message

def find_number_of_encryption_c(encrypted_message, decrypted_message):
    number_of_encryption = 0
    for i in range(0, 26):
        decrypted_message = decrypt_text_c(encrypted_message, i)
        if decrypted_message == encrypted_message:
            number_of_encryption = i
    return number_of_encryption

def find_uncrypted_text_c(encrypted_message):
    print('')

def encrypt_text_a(plaintext,a,b):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) * a + b-65) % 26 + 65)
        else:
            ans += chr((ord(ch) * a + b-97) % 26 + 97)
    return ans

def decrypt_text_a(encrypted_message, a, b):
    letters="abcdefghijklmnopqrstuvwxyz"
    decrypted_message = ""

    for ch in encrypted_message:
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - b) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch
    return decrypted_message

def find_number_of_encryption_a(encrypted_message, decrypted_message):
    number_of_encryption = []
    for i in range(0, 100):
        for k in range(0, 100):
            decrypted_message = decrypt_text_a(encrypted_message, i,k)
            if decrypted_message == encrypted_message:
                number_of_encryption = [i,k]
    return number_of_encryption

def find_uncrypted_text_a(encrypted_message):
    print('')

text_from_plain = take_text_from_file("plain.txt")
text_from_key = take_text_from_file("key.txt")
text_from_extra = take_text_from_file("extra.txt")

encrypt_cesar = text_from_key[0]
parameters_of_anifinic = [text_from_key[2], text_from_key[4]]


match typeCrypt:
    case "-c":
        match typeAction:
            case "-e":
                # crypt cesar code
                print(encrypt_text_c(text_from_plain, encrypt_cesar))
            case "-d":
                # decrypt cesar code
                print(decrypt_text_c(text_from_plain, encrypt_cesar))
            case "-j":
                # cryptoanalysis cesar code
                print(find_number_of_encryption_c(text_from_plain, text_from_extra))
            case "-k":            
                # crypt cesar code with key
                print('')
    case "-a":    
        match typeAction:
            case "-e":
                print(encrypt_text_a(text_from_plain, parameters_of_anifinic[0], parameters_of_anifinic[1]))
            case "-d":
                print(decrypt_text_a(text_from_plain, parameters_of_anifinic[0], parameters_of_anifinic[1]))
            case "-j":
                print(find_number_of_encryption_a(text_from_plain, text_from_extra))
            case "-k": 
                print('')
    case _ : 
        print('')            

