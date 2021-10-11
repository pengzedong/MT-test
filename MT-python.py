import sys


def add(a, b):
    
    #print('the a is', a)
    #print('the b is', b)
    c=int(a)+int(b)
    return print(c)


    
    
if __name__ == '__main__':
    try:
        a, b= sys.argv[1:3]
        add(a, b)
    except Exception as e:
        print(sys.argv)
        print(e)