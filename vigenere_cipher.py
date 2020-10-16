import string
import sys

alphabet = list(string.ascii_uppercase)

def process_key():
    global key
    key = []

    for i in range(0,26):
        temp_list = []
        for j in range(i, i+26):
            temp_list.append(alphabet[j%26])
        key.append(temp_list)

def encode_plaintext_letter(input, key_letter):
    #math to do: add then mod if u need to
    column = key_letter.index(alphabet)
    row = input.index(alphabet)

def find_repeating_groups(cipher):
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
                instances.append(next - first)



if __name__ == '__main__':
    #encode_plaintext_letter('a')
    repetition = find_repeating_groups(ciphertext)
    find_length(repetition)
