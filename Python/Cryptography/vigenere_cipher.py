# 'Hello BeCode! This text has not been encrypted yet.'
# 'programmingissocool'

my_direction = int(input('Do you want to encrypt (1) or decrypt (-1)?\n'))
my_key = input('What is the key?\n')
my_text = input('What do you want to encrypt/decrypt?\n')

def vigenere(text, key, direction):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_text = ''

    for char in text.lower():

        # Append any non-letter character to the text
        if not char.isalpha():
            final_text += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            
            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_text += alphabet[new_index]
        
    print('_'*int(len(text)*1.4), '\nInput text:', text, '\n')
    print('Output text:', final_text, '\n', '_'*int(len(text)*1.4))
    
    return final_text

vigenere(my_text, my_key, my_direction)


# wvzrf bqowqk! bzag vsle wrg tft nqma kvujmrhso nvh.