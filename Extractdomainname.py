#!/usr/bin/python3
#_*_ coding : utf-8 _*_  .rfind("/")
def SplitStrings(url):
    if url.startswith('h') and not url.count('www'):
        idx = url.index(':') + 3
        idx2 = url.index('.')
        # return url[idx:idx2]
        print(url[idx:idx2])
    elif url.startswith('h') and url.count('www'):
        idx = url.index('.') + 1       
        idx2 = url.index('.', idx+1)
        print(url[idx:idx2])
    elif url.startswith('w'):
        idx = url.index('.') + 1  
        idx2 = url.index('.', idx+1)
        # return url[idx:idx2]
        print(url[idx:idx2])
        
if __name__ == '__main__':
    SplitStrings("http://google.com")
    SplitStrings("http://google.co.jp")
    SplitStrings("www.xakep.ru")
    SplitStrings("https://youtube.com")
    SplitStrings("http://github.com/carbonfive/raygun")
    SplitStrings("http://www.zombie-bites.com")
    SplitStrings("https://www.cnet.com")
    print('Hello Python!')