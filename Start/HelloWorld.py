import sys
import Student

print("HelloWorld")

yoga = Student.Student()
yoga.name = "Yoganand"
print("Hello " + yoga.name)
print("ToStr -> {}".format(yoga))

print("******** LIST ********")
numList = [1, 56, 3, 57, 9, 346, 56, 54645, 123443, 567, 56, 33]
print("numList -> ", end='')
print(*numList)
print("Max -> %d" % max(numList))
print("Min -> %d" % min(numList))
print("Length -> %d" % len(numList))
print("Count(56) -> %d" % numList.count(56))
print("Count(1) -> %d" % numList.count(1))

print("*********TUPLE*********")
tupleEg = ('yoga', 'kiruba', 'Saroja',)
print("Tuple ->" + str(tupleEg))

print("******** Dictionary ********")
ageDictionary = {"Yoga": 23, "Kiruba": 25, "Vignesh": 26}
print(*ageDictionary)
ageDictionary.pop("Yoga")
ageDictionary["Kiruba"] = 21
del (ageDictionary["Vignesh"])
print(*ageDictionary)
print(ageDictionary.keys())
print(ageDictionary.values())
