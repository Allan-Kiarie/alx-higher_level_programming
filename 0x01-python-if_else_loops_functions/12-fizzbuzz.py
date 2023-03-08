#!/usr/bin/python3
def fizzbuzz():
    '''Prints numbers from 1 to 100 separated by a space.
    If the number is a multiple of 3 print Fizz instead of the number.
    If the number is a multiple of 5 print Buzz instead of the number.
    If the number is a multiiple of both 3 and 5 print FizzBuzz instead of the number.
    '''
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ")
        elif number % 3 == 0:
            print("Fizz ")
        elif number % 5 == 0:
            print("Buzz ")
        else:
            print("{} ".format(number))
