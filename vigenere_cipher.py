import string
import sys

alphabet = list(string.ascii_uppercase)

def process_inputs():
    if len(sys.argv) < 3:
        sys.exit()

    #args from command line
    global encode, text, key
    mode = sys.argv[1]
    if mode == 'encode':
        encode = True
    else:
        encode = False
    text = sys.argv[2].upper()
    key = sys.argv[3]

    #print the ciphertext and the key
    print("\nThe ciphertext is: " + text)
    print("The key is: " + key)

def encode_plaintext_letter(input, key_letter):
    #math to do: add then mod if u need to
    column = key_letter.index(alphabet)
    row = input.index(alphabet)

def vigenere_cipher(text, key, encode):
    broken_up = []
    key_length = len(key)
    for i in range(key_length):
        broken_up.append(text[i::key_length])
    print(broken_up)

if __name__ == '__main__':
    process_inputs()
    vigenere_cipher(text, key, encode)


'''def find_repeating_groups(cipher):
    repetitive_trios = []
    for i in range(0, len(cipher) - 3):
        instances = 0
        current_trio = cipher[i] + cipher[i+1] + cipher[i+2] + cipher[i+3]
        for i in range(i, len(cipher) - 3):
            check_trio = cipher[i] + cipher[i+1] + cipher[i+2] + cipher[i+3]
            if current_trio == check_trio:
                instances+=1
        if instances > 2 and (current_trio not in repetitive_trios):
            repetitive_trios.append(current_trio)
    return repetitive_trios

def find_length(groups):
    for current in groups:
        first_instance = True
        first = 0
        instances = []
        for i in range(i, len(cipher) - 3):
            next = 0
            check = cipher[i] + cipher[i+1] + cipher[i+2] + cipher[i+3]
            if current == check:
                if first_instance:
                    first = cipher[i]
                    first_instance= False
                else:
                    next = cipher[i]
            if not first_instance:
                instances.append(next - first)'''
