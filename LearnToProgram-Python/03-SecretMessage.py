user_input = input("Enter the message to be encrypted : ")

encrypted_str = []
for char in user_input:
    print("{} -> {}".format(char, str(ord(char))))
    encrypted_str.append(ord(char))

print("encrypted word -> {}".format(''.join(str(x) for x in encrypted_str)))

unencrypted_str = []
for char in encrypted_str:
    unencrypted_str.append(chr(char))

print("Unencrypted word -> {}".format(''.join(unencrypted_str)))
