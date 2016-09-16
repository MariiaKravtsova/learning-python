""" Converter Calculator """

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Pounds to Kilograms')
    print('4. Kilograms to Pounds')


def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers {0}'.format(km))

def pounds_kg():
    pounds = float(input('Enter weight in pounds: '))
    kg = pounds * (1/2.2)
    print('Weight in kilograms is {0}'.format(kg))

def kg_pounds():
    kg = float(input('Enter weight in kilograms: '))
    pounds = kg * 2.2
    print('Weight in pounds is {0}'.format(pounds))

if __name__=='__main__':
    print_menu()
    choice = int(input('Which conversion would you like to do? '))
    if choice == 1:
        km_miles()
    if choice == 2:
        miles_km()
    if choice == 3:
        pounds_kg()
    if choice == 4:
        kg_pounds()
