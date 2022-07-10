#InputMeiGuiShu.py
a,b,c,d,sum=0,0,0,0,0
for i in range(1000,10000):
    a=i%10
    b=(i%100-a)/10
    c=(i%1000-i%100)/100
    d=i//1000
    sum=pow(a,4)+pow(b,4)+pow(c,4)+pow(d,4)
    if sum==i:
        print(i)