from hashlib import md5
from PIL import Image

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ''        

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def split_into_blocks(data, block_size):
    return [data[i:i + block_size] for i in range(0, len(data), block_size)]

def encrypt_ecb(plaintext, key):
    blocks = split_into_blocks(plaintext, len(key))
    ciphertext = b''
    for block in blocks:
        ciphertext += xor_bytes(block, key)
    return ciphertext

def encrypt_cbc(plaintext, key, iv):
    blocks = split_into_blocks(plaintext, len(key))
    ciphertext = b''
    prev_block = iv
    for block in blocks:
        encrypted_block = xor_bytes(block, prev_block)
        encrypted_block = xor_bytes(encrypted_block, key)
        ciphertext += encrypted_block
        prev_block = encrypted_block
    return ciphertext

def process_image(input_path, output_ecb_path, output_cbc_path, key):
    with Image.open(input_path) as img:
        pixels = img.load()
        width, height = img.size
        data = b''

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                data += bytes([r, g, b])

        key = md5(key.encode()).digest()
        iv = md5(key).digest()

        ecb_data = encrypt_ecb(data, key)
        cbc_data = encrypt_cbc(data, key, iv)

        ecb_img = Image.frombytes(img.mode, img.size, ecb_data)
        ecb_img.save(output_ecb_path)

        cbc_img = Image.frombytes(img.mode, img.size, cbc_data)
        cbc_img.save(output_cbc_path)

input_path = 'plain.bmp'
output_ecb_path = 'ecb_crypto.bmp'
output_cbc_path = 'cbc_crypto.bmp'

if (read_file('key.txt') == ''):
    key = 'moj_tajny_klucz'
key = read_file('key.txt')

process_image(input_path, output_ecb_path, output_cbc_path, key)