import random

while True:

    num1 = random.randint(1, 30)
    num2 = random.randint(1,30)
    saiso = random.randint(-3, 3)

    sum= num1 + num2 + saiso

    print("{} + {} = {}".format(num1, num2, sum))

    answer = input("T or F?").lower()

    if answer == "t":
        if saiso == 0:
            print("Correct")
        else:
            print("Wrong")
    else:
        if saiso != 0:
            print("correct")
        else:
            print("false")


