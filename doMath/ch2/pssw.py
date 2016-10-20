import random, string

def getNumber():
    return random.randrange(0, 9, 1)

def getLetter():
    return random.choice(string.ascii_letters)

result = ''
for i in range(1, 9, 1):
    if i == 0 or i == 1 or i == 4 or i == 5:
        result = result + str(getLetter())
    elif i == 8:
        result = result + '#'
    else:
        result = result + str(getNumber())

print(result.lower())
