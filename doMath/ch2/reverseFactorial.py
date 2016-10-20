import numpy
import timeit
import os

def reverseFactorial(myinput):

    result = 1
    i = 0

    while (result < myinput):
        string = ' '
        os.system('clear')
        start = timeit.default_timer()
        i = i + 1
        result = i * result
        stop = timeit.default_timer()
        number1 = numpy.random.randint(0, 10)
        number2 = numpy.random.randint(0, 100)
        for j in range(0, number2):
            print()
        for k in range(0, number1):
            string += string
        print(string, "Make America Great Again!")

y = 678435970 * (10**99999)
reverseFactorial(y)
