#!/usr/bin/python3
#_*_ coding : utf-8 _*_ 

# # approach 1:
# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
# # approach 2:
# def pig_it(text):
#     return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

def SimplePigLatin(s):
    if s.count(' ') == 0:
        if s.count(' ') == 0:
            # print('Oay emporatay oay oresmay !')
            # return '0ay'
            print('0ay')
     
    lis = s.split(' ')
    lis1 = []
    str_tmp = ''

    for i in range(len(lis)):
        print('lis[i]', lis[i])
        if len(lis[i]) >= 2:
            if lis[i][0].isalpha():
                str_tmp = lis[i][1:] + lis[i][0] + 'ay'
            lis1.append(str_tmp)
        elif lis[i].isalpha():
                str_tmp = lis[i] + 'ay'
                lis1.append(str_tmp)    
        else:
            lis1.append(lis[i])
    str_tmp = ''.join(t + ' ' for t in lis1)[:-1]
    print(lis1)
    print(str_tmp)

if __name__ == '__main__':
    # "O tempora o mores !": 'O emporatay o oresmay !'
    SimplePigLatin("O tempora o mores !")
    SimplePigLatin('Pig latin is cool')
    SimplePigLatin('Hello world !')
    print('Hello Python!')