#!/usr/bin/python3
#_*_ coding : utf-8 _*_
# import re

# pattern = re.compile('^[0-9a-zA-Z]+$')

# def alphanumeric(string):
#   return pattern.match(string) is not None
def alphanumeric(s):
    if len(s) == 0:
        return False
    else:
        return s.isalnum()

if __name__ == '__main__':
    assert(alphanumeric("hello world_"))

    print('Hello Python!')