""" Determine if integer is even or odd """

def is_even(x):
    if x % 2 == 0:
        print('The number is even.')
    else:
        print('The number is odd.')

if __name__=='__main__':
    answer = float(input('Enter a number: '))

    is_even(answer)
