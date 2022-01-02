print('Welcome to my Maths Calculation app ')
print('My most boring work is to do calculations . ')
print('So, I have created maths calculation app .')
print('Press 1 to plus')
print('Press 2 to sunstract ')
print('Press 3 to multiply')
print('Press 4 to divide')
number = int(input('Enter your choice'))

def multipl() :
    print('You have choosen multiply')
    number1 = int(input('Enter your first number'))
    number2= int(input('Enter your second number'))
    print('Your answer is ')
    mul = number1 * number2
    print(mul)
def add() :
    print('You have choosen plus')
    number1 = int(input('Enter your first number'))
    number2= int(input('Enter your second number'))
    print('Your answer is ')
    ad = number1 + number2
    print(ad)
def substract() :
    print('You have choosen minus')
    number1 = int(input('Enter your first number'))
    number2= int(input('Enter your second number'))
    print('Your answer is ')
    sub = number1 - number2
    print(sub)
def divide() :
    print('You have choosen divide')
    number1 = int(input('Enter your first number'))
    number2= int(input('Enter your second number'))
    print('Your answer is ')
    div = number1 / number2
    print(div)

if number == 1 :
    add()
if number == 2 :
    substract()
if number == 3 :
    multipl()
if number == 4 :
    divide()
