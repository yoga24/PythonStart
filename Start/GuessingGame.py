import random

print("Guessing Game!")
invalidInput = True
userNum = 0
while invalidInput:
    userNum = int(input("Enter a number 0 - 100 : "))
    if userNum < 0 or userNum > 100:
        invalidInput = True
    else:
        invalidInput = False

beginIndex = 0
lastIndex = 100
counter = 0

while True:
    counter = counter + 1
    compNum = random.randint(beginIndex, lastIndex)
    print("Computer Guess : "+str(compNum))
    if compNum < userNum:
        beginIndex = compNum + 1
        print("Computer Guess is lower. Re-Guessing with Range:"+str(beginIndex)+"-"+str(lastIndex))
    elif compNum > userNum:
        lastIndex = compNum - 1
        print("Computer Guess is higher. Re-Guessing with Range:" + str(beginIndex) + "-" + str(lastIndex))
    else:
        print("Computer Guessed Correctly in "+str(counter)+" turn(s)!!! ")
        break
