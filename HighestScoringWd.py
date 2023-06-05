#!/usr/bin/python3
#_*_ coding : utf-8 _*_

# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
def HighestScoringWd(s):
    dict1 = {chr(97+i):i+1 for i in range(26)}
    lis = s.split(' ')
    idx = 0
    cnt = 0
    imax = 0
    print(lis)

    for t in lis:
        for i in range(len(t)):
            if t[i].isalpha():
                cnt += dict1[t[i]]
        if imax < cnt:
            imax = cnt
            idx = lis.index(t)
        cnt = 0

    print(lis[idx])        

    # print(dict1)
    
if __name__ == '__main__':
    HighestScoringWd('man i need a taxi up to ubud')
    HighestScoringWd('what time are we climbing up the volcano')
    HighestScoringWd('take me to semynak')
    print('Hello Python!')