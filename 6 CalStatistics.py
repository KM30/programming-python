#CalStatistics.py

def GetNum():
    ls=[]
    iNumStr=input('请输入数字(回车退出)：')
    while iNumStr !='' :
        ls.append(eval(iNumStr))
        iNumStr=input('请输入数字(回车退出)：')
    return ls

def CalMean(List):
    s=0
    for num in List:
        s+=num
    mean1=s/(len(List))
    return mean1

def CalDev(average,ls):
    total=0
    for c in ls:
        sub=c-average
        total+=pow(sub,2)
    mean2=total/(len(ls)-1)
    dev=pow(mean2,0.5)
    return dev

def FinMedian(ls):
    sorted(ls)
    size=len(ls)
    if size%2==0:
        med=(ls[size//2-1]+ls[size//2])/2
    else:
        med=ls[size//2]
    return med

def main():
    l=GetNum()
    m=CalMean(l)
    d=CalDev(m,l)
    me=FinMedian(l)
    print('平均值：{}，方差：{:.2}，中位数：{}'.format(m,d,me))

main()
        
        
