userNum = input("Enter a number or 'q' to quit: ")
total = 0
# this loop stores each user input into total and adds to the previous total, then prints overall total
while (userNum != "q"):
    total = total + int(userNum)
    userNum = input("Enter another number or 'q' to quit: ")
print(total)


userInput = ""
# this will count up or down based on user input by inputting into a for range loop
while (userInput != 'q'):
    userInput = input("Enter 1 for 'count down', 2 for 'count up' or 'q' to quit: ")
    if userInput == "1":
        countDown = int(input("What negative number would you like to count down to? "))
        for x in range(0, countDown-1, -1):
            print(x)
    elif userInput == "2":
        countDown = int(input("What number would you like to count up to? "))
        for x in range(0, countDown+1, 1):
            print(x)

# asks user for both ends of a counting range and will know to count up or down based on the order they are input
countFrom = int(input("Enter a number you want to count from: "))
countTo = int(input("Enter a number you want to count to: "))
for x in range(countFrom, countTo+1):
    print(x)
for x in range(countFrom, countTo-1, -1):
    print(x)