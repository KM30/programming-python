#daydayup.py

#函数
def DayUp(df,rf):
    dayup=1.0
    for i in range(365):
        if i%7 in [6,0]:
            dayup*=1-rf
        else:
            dayup*=1+df
    return dayup
#输入
dayfactor=eval(input("df:"))
restfactor=eval(input("rf:"))
#循环
ed=round(pow(1+dayfactor,365),2)
while DayUp(dayfactor,restfactor)<ed:
    dayfactor+=0.001
#输出
print("工作日向上的参数：{:.3f}\n".format(dayfactor))
print("工作日向上的总量：{:.3f}\n".format(DayUp(dayfactor,restfactor)))
