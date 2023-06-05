#!/usr/bin/python3
#_*_ coding : utf-8 _*_
# Replace With Alphabet Position

def alphabet_position(s):
    # dict1 = {chr(97+i):i+1 for i in range(26)}
    # lis = []
    # lis1 = []
    str_tmp = ''
    for w in s.split(' '):
        for i in range(len(w)):
            if w[i].isalpha():
                # lis1.append(w[i])
                # lis.append(ord(w[i].lower()) - ord('a') + 1)
                str_tmp += str(ord(w[i].lower()) - ord('a') + 1) + ' '
    str_tmp = str_tmp[:-1]
    # print(lis1)
    # print(lis)
    # print(str_tmp)
    return str_tmp



if __name__ == '__main__':
    alphabet_position("The sunset sets at twelve o' clock.")
    print('Hello Python!')