#CalPi.py
import time as t
import random as r

DATAS=eval(input('撒点数：'))
start=t.perf_counter()
r.seed(123)
hits=0
for i in range(DATAS):
    x,y=r.random(),r.random()
    dist=pow(pow(x,2)+pow(y,2),0.5)
    if dist<=1:
        hits+=1
pi=4*(hits/DATAS)
end=t.perf_counter()
print('圆周率：{:.6f}'.format(pi))
print('运行时间：{:.2f}s'.format(end-start))