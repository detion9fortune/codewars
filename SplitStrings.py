#!/usr/bin/python3
#_*_ coding : utf-8 _*_

# import re

# def solution(s):
#     return re.findall(".{2}", s + "_")

def SplitStrings(str):
    str1 = str
    lis = []

    if len(str) % 2 == 1:
        str1 += '_'
    
    print(str1)
    # for i in range(0, len(str1), 2):
    #     # print(i)
    #     lis.append(str1[i] + str1[i+1])

    # lis = [t for t in (str1[i] + str1[i+1] for i in range(0, len(str1), 2))]
    lis = [str1[i:i+2] for i in range(0, len(str1), 2)]

    print(lis)

if __name__ == '__main__':
    SplitStrings('abc')
    print('Hello Python!')