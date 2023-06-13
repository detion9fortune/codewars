#!/usr/bin/python3
#_*_ coding : utf-8 _*_
# print("{:02x}".format(148))
# 当从image中获得RGB是 负数 的时候，用下面的公式转换成正数
# newR=255-oldR newG=255-oldG newB=255-oldB

# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))

def rgbtohex(num1,num2,num3):
    r, g, b = num1, num2, num3
    if num1 < 0:
        r = 0
    elif num1 > 255:
        r = 255 
    if num2 < 0:
        g = 0
    elif num2 > 255:
        g = 255    
    if num3 < 0:
        b = 0
    elif num3 > 255:
        b = 255  
    print("{:02X}{:02X}{:02X}".format(r,g,b))
    # map(lambda t:"{:02x}".format(t),[num1,num2,num3])
    str1 = ''.join("%02X" % t for t in (r,g,b))
    print(str1)

    return "{:02X}{:02X}{:02X}".format(r,g,b)
    

if __name__ == '__main__':
    t1 = rgbtohex(148,0,211)
    print('t1 = %s' % t1)

    t2 = rgbtohex(-235,275,125)
    print('t1 = %s' % t2)

    print('Hello Python!')
