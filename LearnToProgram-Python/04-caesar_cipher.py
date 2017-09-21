# Caesar Cipher -->
# In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift,
# is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which
# each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private correspondence.

# Unicode Functions
# A - Z : 65 - 90
# a - z : 97 - 122
# ord(character) -> returns unicode number
# chr(number) -> returns character

input_str = input("Enter the string to be encrypted : ")

shift_pos = 0
while True:
    try:
        shift_pos = int(input('Enter the cipher shift position count : '))
        if shift_pos < 0 or shift_pos > 26:
            raise ValueError('Cipher shifting position should be between 0-26')
        break
    except ValueError as exception:
        print('Invalid Value entered! {}. Retry.'.format(exception))

ciphered_str = ''
for char in input_str:
    new_char = char
    if char.isalpha():
        unicode = ord(char) + shift_pos
        if (char.isupper() and unicode > ord('Z')) or (char.islower() and unicode > ord('z')):
            unicode -= 26
        new_char = chr(unicode)
    ciphered_str += new_char

print('Ciphered String - {}'.format(ciphered_str))
