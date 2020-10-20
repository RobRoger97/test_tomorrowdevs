#import randint from random
from random import randint

#define random_Pass
def random_Pass():

    r1 = randint(7, 10)
    x = 0
    res = ''
    while x<=r1:
        r2 = randint(33, 126)
        a = chr(r2)
        res = res+a
        x = x+1

    return res

#define main
def main():
#display the result
    print(random_Pass())

if __name__ == "__main__":
        main()