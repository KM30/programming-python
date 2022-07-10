#Unicode.py
uni=eval(input('Input a number[0,1114111]:'))
for i in range(0,100,10):
    print(chr(uni+i)+' ',end='')