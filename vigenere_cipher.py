import string
import sys

alphabet = list(string.ascii_uppercase)
alphabet_freq = {
    'a': 0.08167, 'b': 0.014920, 'c': 0.02782, 'd': 0.04253, 'e':0.12702, 'f':0.02228, 'g':0.02015, 'h':0.06094, 'i':0.06966, 'j':0.00153, 'k':0.00772, 'l':0.04025, 'm':0.02406, 'n':0.06749, 'o':0.07507, 'p':0.01929, 'q':0.00095, 'r':0.05987, 's':0.06327, 't':0.09056, 'u':0.02758, 'v':0.00978, 'w':0.02360, 'x':0.00150, 'y':0.01974, 'z':0.00074
}

#process command line arguments
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
    key = sys.argv[3].upper()

    #print the ciphertext and the key
    print("\nThe key is: " + key)

#function to break up text for frequency analysis
def break_up_text(text, key):
    broken_up = []
    key_length = len(key)
    for i in range(key_length):
        substring = key[i::key_length]
        broken_up.append(substring)
    return broken_up

#encode/decode functino
def vigenere_cipher(text, key, encode):
    count = 0
    key_length = len(key)
    cipher_text = ''

    for char in text:
        current_index = alphabet.index(char)
        current_shift = alphabet.index(key[count % key_length])
        if encode:
            new_char = alphabet[(current_index + current_shift) % 26]
        else:
            new_char = alphabet[(current_index - current_shift) % 26]
        cipher_text+=new_char
        count+=1

    print("\nYour ciphertext is: \"" + cipher_text + "\"\n")

if __name__ == '__main__':
    process_inputs()
    vigenere_cipher(text, key, encode)
