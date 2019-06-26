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

def getRange():
    # function to get two integers from user that will find all the 
    # prime numbers in said range
    print("Give me a range of numbers and find out which numbers in the")
    print("range are prime numbers?")
    firstNumber = getPrime()
    secondNumber = getPrime()

    primeList = []
    if firstNumber < secondNumber:
        primeList = rangeOfPrime(firstNumber, secondNumber)
    else:
        primeList = rangeOfPrime(secondNumber, firstNumber)
    
    return primeList

def rangeOfPrime(num1, num2):
    # function that iterates though the range of numbers given to
    # find the prime numbers and return a list of said primes.

    listOfPrimes = [] 
    for element in range(num1, num2+1):
        if isPrime(element):
            listOfPrimes.append(element)
    return listOfPrimes

def nextHundredPrimes():
    # Function that will find the next 100 prime numbers from an integer
    # asked for from the user.

    print("Give me a number.")
    userNumber = getPrime()
    if isPrime(userNumber):
        print(f"{userNumber} is a prime number.")
    else:
        print(f"{userNumber} is not a prime number.")

    
    listOfPrimes = []
    primeStart = userNumber
    
    while (len(listOfPrimes) < 100):
        primeStart += 1
        if isPrime(primeStart):
            listOfPrimes.append(primeStart)
    
    return listOfPrimes



userNumber = getPrime()
print(userNumber)

if isPrime(userNumber):
    print(f"{userNumber} is a Prime")
else:
    print(f"{userNumber} is not a Prime")

print()
print()

primeRange = getRange()
print(f"The list of primes are {primeRange}")

print()
print()

oneHundredPrimes = nextHundredPrimes()
# print(f"Length is {len(oneHundredPrimes)}")
print(f"The list of next 100 primes are {oneHundredPrimes}")