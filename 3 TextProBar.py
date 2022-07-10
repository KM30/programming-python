#TextPro.py

import time

scale=20
print('执行开始'.center(26,'-')+'\n')
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=i*5
    dur=time.perf_counter()-start
    print('\r{:>3}%[{}{}]{:.2f}s'.format(c,a,b,dur))
    time.sleep(0.1)
print('\n'+'执行结束'.center(26,'-'))