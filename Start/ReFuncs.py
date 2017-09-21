import re

string = "This is some gibberish string just for testing the re module"

pos = re.search("some", string)
print(str(pos.start()))
print(str(pos.end()))

print(string[pos.start():pos.end()])

print("This is a {} {}".format('formatted', 'string'))
