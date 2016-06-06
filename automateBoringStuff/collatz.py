def collatz(number):
    while number > 1:
        if (number % 2 == 0):
            number = number // 2
            print(str(number))
        elif (number % 2 == 1):
            number = 3 * number + 1
            print(str(number))
print('Enter your number:')
userNumber = int(input())
collatz(userNumber)

def some(a, b):
    print(a * b)
some(4,5)
