#!/usr/bin/python3
def fizzbuzz():
    '''Prints numbers from 1 to 100 separated by a space.
    If the number is a multiple of 3 print Fizz instead of the number.
    If the number is a multiple of 5 print Buzz instead of the nummber
    Print FizzBuzz instead of the number for multiples of 3 and 5.
    '''
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
