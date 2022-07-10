#daydayup.py
def DayUp(df):
    dayup=1.0
    for i in range(365):
        if i%7 in [6,0]:
            dayup*=1-0.01
        else:
            dayup*=1+df
    return dayup
dayfactor=0.01
while DayUp(dayfactor)<37.78:
    dayfactor+=0.001
print("工作日向上的参数：{:.3f}\n".format(dayfactor))
print("工作日向上的总量：{:.3f}\n".format(DayUp(dayfactor)))