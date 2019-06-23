'''
Function used to accept input from user
'''
def getPrime():
    aNumber = input("Please enter a number: ")
    loopLogic = True
    while loopLogic == True:
        try:
            properNumber = int(aNumber)
            loopLogic = False
        except ValueError:
            print(f"The value entered is not an integer")
            aNumber = input("Please enter a new value: ")


    return properNumber

'''
Function used to check if number is a prime
'''
def isPrime(number):
    # Logic control isPrime = False
    isPrime = False
    if number == 1:
        isPrime = False
    elif number == 2:
        isPrime = True
    else:
        for element in range(2, number//2+1):
            if number % element == 0:
                isPrime = False
                break
            else:
                isPrime = True

    return isPrime

userNumber = getPrime()
print(userNumber)

if isPrime(userNumber):
    print(f"{userNumber} is a Prime")
else:
    print(f"{userNumber} is not a Prime")
