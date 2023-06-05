#!/usr/bin/python3
#_*_ coding : utf-8 _*_
def Countcharacters(s):
    # dict1 = {}
    # if(len(s) == 0):
    #     return {}
    
    # for i in range(len(s)):
    #     if s[i].isalpha():
    #         if s[i] in dict1:
    #             dict1[s[i]] += 1
    #         else:
    #             dict1[s[i]] = 1    

    dict1 = {k: list(s).count(k) for k in list(s) if k.isalpha()}

    print(dict1)

if __name__ == '__main__':
    Countcharacters('/+_a')
    print('Hello Python!')