#!/usr/bin/python3

if __name__ == "__main__":
    '''prints the result of the addition of all arguments'''
    from sys import argv

    count = len(argv) - 1
    sum = 0

    for i in range(1, count + 1):
        sum += int(argv[i])
    print("{}".format(sum))
