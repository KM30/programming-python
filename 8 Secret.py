import random

def genpwd(length):
    sec=''
    for i in range(length):
        num=random.randint(0,9)
        sec+=str(num)
    return sec

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
