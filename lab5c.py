#!/usr/bin/env python3
# Author ID: Vishesh1

def add(number1, number2):
    try:
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except (OSError, FileNotFoundError, PermissionError, IsADirectoryError):
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                        # works
    print(add('10', 5))                      # works
    print(add('abc', 5))                     # exception
    print(read_file('seneca2.txt'))          # works
    print(read_file('file10000.txt'))        # exception
