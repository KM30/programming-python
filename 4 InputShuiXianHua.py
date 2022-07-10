#InputShuiXianHua.py
s=''
for i in range(100, 1000):
    t = str(i)
    sum=pow(eval(t[0]),3) + pow(eval(t[1]),3) + pow(eval(t[2]),3)
    if sum == i :
        s += t+','
print(s[:-1])