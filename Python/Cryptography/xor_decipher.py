"""
This script takes a string and a number as input
and returns the result of the XOR operation
between the binary values of the string and the binary value of the number.
"""

cypher = "label"
num = 13


def string_to_binary(a):
    return ''.join(format(ord(i), '08b') for i in a)

def decimal_to_binary(a):
    return format(a, '08b')

# creates list of binary values for each character in the cypher
binary_char = []
for char in cypher:
    binary_char.append(string_to_binary(char))

# converts num to binary
binary_num = decimal_to_binary((num))

# xor the binary values of the cypher with the binary value of the num
def xor(a, b):
    xor_result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            xor_result += '0'
        else:
            xor_result += '1'
    return xor_result

# apply xor function to each element in binary_char
final_result = ''
for element in binary_char:
    final_result += xor(element, binary_num)
    print(final_result)

# converts final_result back to ascii
def binary_to_string(a):
    return ''.join(chr(int(a[i:i+8], 2)) for i in range(0, len(a), 8))

print(binary_to_string(final_result))
