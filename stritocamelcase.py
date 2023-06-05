#!/usr/bin/python3
#_*_ coding : utf-8 _*_
def SplitStrings(str):
    str1 = str
    str_tmp = ''
    for i in range(len(str1)):
        if not str1[i] in ('_','-'):
            if str1[i-1] in ('_','-'):
                str_tmp += str1[i].upper()
            else:
                str_tmp += str1[i]   

      
    print(str_tmp)
if __name__ == '__main__':
    SplitStrings("The_Stealth-Warrior")
    print('Hello Python!')