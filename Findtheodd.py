#!/usr/bin/python3
#_*_ coding : utf-8 _*_ 

# # approach 1:
# def find_it(seq):
#     return [x for x in seq if seq.count(x) % 2][0]
# # approach 2:
# import operator

# def find_it(xs):
#     return reduce(operator.xor, xs)
# # approach 3:
# from collections import Counter
# def find_it(l):
#     return [k for k, v in Counter(l).items() if v % 2 != 0][0]

# # approach 4:
# def find_it(seq):
#     for elem in set(seq):
#         if seq.count(elem) % 2 == 1:
#             return elem

from collections import Counter

def Findtheodd(seq):
    if len(seq) == 1:
        return seq[0]
    
    cnt = Counter(seq)
    # print(cnt)
    for k, v in cnt.items():
        if v % 2 == 1:
            print(k)

if __name__ == '__main__':
    # "O tempora o mores !": 'O emporatay o oresmay !'
    Findtheodd([1,1,2])
    print('Hello Python!')    
