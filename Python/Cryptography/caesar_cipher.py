# 'Hello BeCode! This text has not been encrypted yet.'

my_direction = int(input('Do you want to encrypt (1) or decrypt (-1)?\n'))
#my_offset = int(input('What is the offset?\n'))
my_text = input('What do you want to encrypt/decrypt?\n')

def caesar(text, offset, direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():

        if not char.isalpha():
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            encrypted_text += alphabet[new_index]
            
    print('_'*int(len(text)*1.4), '\nInput text:', text, '\n')
    print('Output text:', encrypted_text, '\n', '_'*int(len(text)*1.4))

    return encrypted_text

for i in range(26):
    my_offset = i
    caesar(my_text, my_offset, my_direction)


# 'khoor ehfrgh! wklv whaw kdv qrw ehhq hqfubswhg bhw.' (my_offset = 3)