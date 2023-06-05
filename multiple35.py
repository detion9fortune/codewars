#!/usr/bin/python3
#_*_ coding : utf-8 _*_

# best approach 
# def multiple35(num):
# return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

def multiple35(num):
    lis = []
    if num <=3:
        return 0
    
    for i in range(1,num+1):
        if num > i * 3:
            if not lis.count(i * 3):
                lis.append(i * 3)
            if num > i * 5:
                if not lis.count(i * 5):
                    lis.append(i * 5)
        else:
            lis.append(0)
            break            
    # return sum(lis)
    print(lis)
    print(sum(lis))
    

if __name__ == '__main__':
    multiple35(4)
    print('Hello Python!')
